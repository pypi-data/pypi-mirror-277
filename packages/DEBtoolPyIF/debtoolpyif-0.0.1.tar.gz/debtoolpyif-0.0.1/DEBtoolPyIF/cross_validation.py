import random
from math import ceil
import matplotlib.pyplot as plt
import time
from collections import defaultdict
import os

from code_generator import GroupStepCodeGenerator, IndividualStepCodeGenerator
from data_sources import IndDataSourceBase
from matlab_wrapper import run_estimation, EstimationRunner


class HoldoutCV:
    # TODO: Redo using latest changes
    def __init__(self, template_folder, individual_pars, group_pars, species_name):
        self.individual_pars = individual_pars
        self.group_pars = group_pars
        self.species_name = species_name

        # Initialization is an estimation without individual params
        self.init_code_generator = IndividualStepCodeGenerator(template_folder, [], species_name)
        self.training_code_generator = IndividualStepCodeGenerator(template_folder, individual_pars, species_name)
        self.testing_code_generator = IndividualStepCodeGenerator(template_folder, individual_pars, species_name)
        self.training_results = {}
        self.testing_results = {}
        self.start_time = 0
        self.elapsed_time = 0
        self.output_folder = None
        self.train_error = []
        self.test_error = []
        self.loss_logfile = None
        self.re_logfile = None

        self.individuals = set()

    def add_data_source(self, data_source: IndDataSourceBase):
        self.init_code_generator.add_data_source(data_source)
        self.training_code_generator.add_data_source(data_source)
        self.testing_code_generator.add_data_source(data_source)
        self.individuals = self.individuals.union(data_source.individuals)

    def train_test_split(self, test_size=0.25):
        random.seed(10)
        ind_list = sorted(list(self.individuals))

        random.shuffle(ind_list)
        n_test = ceil(test_size * len(self.individuals))

        train_inds = sorted(ind_list[n_test:])
        test_inds = sorted(ind_list[:n_test])

        return train_inds, test_inds

    def get_group_pars(self, pars):
        group_pars = {}
        for p in self.group_pars:
            if p in self.individual_pars:
                if p + '_avg' in pars:
                    group_pars[p] = pars[p + '_avg']
                else:
                    group_pars[p] = pars[p]
            else:
                group_pars[p] = pars[p]
        return group_pars

    def fit_predict(self, train_run_settings, test_run_settings, test_size=0.25, output_folder=None, window=False,
                    save=True, hide_output=True):
        # TODO: ind_list as parameter
        # Split dataset
        train_inds, test_inds = self.train_test_split(test_size=test_size)
        # Set up vars and files
        self.train_error = []
        self.test_error = []
        self.start_time = time.time()
        init_output_folder = f"{output_folder}/init"
        training_output_folder = f"{output_folder}/train"
        testing_output_folder = f"{output_folder}/test"
        os.makedirs(init_output_folder)
        os.makedirs(training_output_folder)
        os.makedirs(testing_output_folder)

        # Initialize logs
        if save:
            self.loss_logfile = open(f"{output_folder}/loss_logs.txt", 'w')
            self.re_logfile = open(f"{output_folder}/re_logs.txt", 'w')
            header = "run,time," \
                     "end_train,end_train_0,end_train_1," \
                     "nip_train,nip_train_0,nip_train_1," \
                     "end_test,end_test_0,end_test_1," \
                     "nip_test,nip_test_0,nip_test_1"
            print(header, file=self.loss_logfile)
            print(header, file=self.re_logfile)
        # Connect to MATLAB
        runner = EstimationRunner()

        # Setup run settings for initialization, group pars values are used for initialization
        init_run_settings = train_run_settings.copy()
        init_run_settings['pars_init_method'] = 2
        self.init_code_generator.set_estimation_settings(**init_run_settings)
        self.init_code_generator.generate_code(init_output_folder, self.group_pars, ind_list=train_inds,
                                               estimate_group_pars=1)
        init_results = runner.run_estimation(init_output_folder, self.species_name, window=window,
                                             clear_before=True, hide_output=hide_output)

        # Setup run settings for training, first run loads pars from pars_init.m file
        default_pars = self.get_group_pars(init_results['pars'])
        self.training_code_generator.set_estimation_settings(n_runs=0, results_output_mode=0,
                                                             n_steps=train_run_settings['n_steps'], pars_init_method=2)
        self.training_code_generator.generate_code(training_output_folder, default_pars, ind_list=train_inds,
                                                   estimate_group_pars=1)
        training_results = runner.run_estimation(training_output_folder, self.species_name, window=window,
                                                 clear_before=True, hide_output=hide_output)

        # Generate testing code
        default_pars = self.get_group_pars(training_results['pars'])
        species_data_factor = len(test_inds) / len(train_inds)
        self.testing_code_generator.set_estimation_settings(n_runs=test_run_settings['n_runs'], results_output_mode=0,
                                                            n_steps=test_run_settings['n_steps'], pars_init_method=2)
        self.testing_code_generator.generate_code(testing_output_folder, default_pars, ind_list=test_inds,
                                                  group_data_weight=species_data_factor)
        testing_results = runner.run_estimation(testing_output_folder, self.species_name, window=window,
                                                clear_before=True, hide_output=hide_output)

        # Log errors
        print(f"[{time.ctime()[11:19]}] - Start  .> "
              f"train      all     spcs     inds | test      all     spcs     inds")
        self.log_errors(training_results, testing_results, save=save)

        # Now we set up the next runs
        self.training_code_generator.set_estimation_settings(n_runs=0, results_output_mode=0,
                                                             n_steps=train_run_settings['n_steps'], pars_init_method=1)
        self.training_code_generator.create_run_file(training_output_folder)

        for i in range(1, train_run_settings['n_runs'] - 1):
            training_results = runner.run_estimation(training_output_folder, self.species_name, window=window,
                                                     clear_before=True, hide_output=hide_output)
            # Get the group parameters from training estimation
            default_pars = self.get_group_pars(training_results['pars'])

            # Update pars_init.m file
            self.testing_code_generator.create_pars_init_file(testing_output_folder, default_pars)
            testing_results = runner.run_estimation(testing_output_folder, self.species_name, window=window,
                                                    clear_before=True, hide_output=hide_output)

            # Log errors
            self.log_errors(training_results, testing_results, save=save)

        # Final run
        self.training_code_generator.set_estimation_settings(n_runs=0, pars_init_method=1,
                                                             results_output_mode=train_run_settings['results_output_mode'],
                                                             n_steps=train_run_settings['n_steps'])
        self.training_code_generator.create_run_file(training_output_folder)
        training_results = runner.run_estimation(training_output_folder, self.species_name, window=window,
                                                 clear_before=True, hide_output=hide_output)
        # Get the group parameters from training estimation
        default_pars = self.get_group_pars(training_results['pars'])

        # Update pars_init.m and run.m file
        self.testing_code_generator.set_estimation_settings(n_runs=test_run_settings['n_runs'],
                                                            results_output_mode=test_run_settings['results_output_mode'],
                                                            n_steps=test_run_settings['n_steps'], pars_init_method=2)
        self.testing_code_generator.create_run_file(testing_output_folder)
        self.testing_code_generator.create_pars_init_file(testing_output_folder, default_pars)
        testing_results = runner.run_estimation(testing_output_folder, self.species_name, window=window,
                                                clear_before=True, hide_output=hide_output)

        # Log errors
        self.log_errors(training_results, testing_results, save=save)

        if save:
            self.save_results(self.training_results, default_pars, training_output_folder)
            self.save_results(self.testing_results, default_pars, testing_output_folder)
            self.re_logfile.close()
            self.loss_logfile.close()

    def log_errors(self, training_results, testing_results, save=True):
        self.elapsed_time = time.time() - self.start_time
        self.training_results = training_results
        self.testing_results = testing_results
        time_str = time.ctime(self.elapsed_time)[11:19]
        run_number = len(self.train_error)

        suffixes = ('', '_0', '_1')
        types = ('all', 'spcs', 'inds')
        lossfunctions = ('sb', 're')
        moments = ('final', 'noindpars')
        nested_dict = lambda: defaultdict(nested_dict)
        train_errors_dict = nested_dict()
        test_errors_dict = nested_dict()
        for lf in lossfunctions:
            train_lf_values = []
            test_lf_values = []
            for m in moments:
                for s, t in zip(suffixes, types):
                    train_value = training_results['estimation_errors'][m][lf + s]
                    train_errors_dict[lf][m][t] = train_value
                    test_value = testing_results['estimation_errors'][m][lf + s]
                    test_errors_dict[lf][m][t] = test_value
                    train_lf_values.append(f"{train_value:.6f}")
                    test_lf_values.append(f"{test_value:.6f}")
            if save:
                if lf == 're':
                    print(f"{run_number},{time_str},{','.join(train_lf_values)},{','.join(test_lf_values)}",
                          file=self.re_logfile)
                elif lf == 'sb':
                    print(f"{run_number},{time_str},{','.join(train_lf_values)},{','.join(test_lf_values)}",
                          file=self.loss_logfile)

        self.train_error.append(dict(train_errors_dict))
        self.test_error.append(dict(test_errors_dict))

        self.print_errors()

    def print_errors(self):
        time_str = time.ctime(self.elapsed_time)[11:19]
        run_number = len(self.train_error)
        # Mean relative errors for training
        train_lf = self.train_error[-1]['sb']['final']['all']
        train_lf_0 = self.train_error[-1]['sb']['final']['spcs']
        train_lf_1 = self.train_error[-1]['sb']['final']['inds']

        # Mean relative errors for testing
        test_lf = self.test_error[-1]['sb']['final']['all']
        test_lf_0 = self.test_error[-1]['sb']['final']['spcs']
        test_lf_1 = self.test_error[-1]['sb']['final']['inds']

        print(f"({time_str}) - Run {run_number:2} .> "
              f"train {train_lf:.6f} {train_lf_0:.6f} {train_lf_1:.6f} | "
              f"test {test_lf:.6f} {test_lf_0:.6f} {test_lf_1:.6f}")

    def save_results(self, results, default_pars, output_folder):
        # Individual params
        ind_pars_dict = {p: [] for p in self.individual_pars}

        uni_variate_data_types = results['meta_data']['univariate_types']
        ind_list = results['meta_data']['inds']
        zero_variate_data_names = results['meta_data']['data_0']
        uni_variate_data_names = results['meta_data']['data_1']
        # Only data with weight greater than zero
        estimation_errors = [e[0] for e in results['estimation_errors']['re'] if e[1] > 0]
        errors = {d: e for d, e in zip(zero_variate_data_names + uni_variate_data_names, estimation_errors)}

        ind_file = open(f'{output_folder}/ind_pars.csv', 'w')
        header = 'id,' + ','.join(self.individual_pars) + ',' + ','.join(
            ['e_' + dt for dt in uni_variate_data_types])
        print(header, file=ind_file)
        for ind in ind_list:
            ind_par_values = [ind]
            for p in self.individual_pars:
                ind_par_var = f"{p}_{ind}"
                value = results['pars'][ind_par_var]
                ind_par_values.append(f"{value:.4f}")
                ind_pars_dict[p].append(value)
            for dt in uni_variate_data_types:
                ind_par_values.append(f"{errors[f'{dt}_{ind}']:.4f}")

            print(','.join(ind_par_values), file=ind_file)
        ind_file.close()

        # Group parameters
        n_inds = len(ind_list)

        group_file = open(f'{output_folder}/group_pars.csv', 'w')
        for gp in default_pars:
            if gp in self.individual_pars:
                print(f"{gp} {sum(ind_pars_dict[gp]) / n_inds:.4f}", file=group_file)
            else:
                print(f"{gp} {results['pars'][gp]:.4f}", file=group_file)
        group_file.close()

        zero_var_data_file = open(f'{output_folder}/zero_var_errors.csv', 'w')
        for zv in zero_variate_data_names:
            print(f"{zv} {errors[zv] * 100:.4f}", file=zero_var_data_file)
        zero_var_data_file.close()

    def plot_errors(self, error_type):
        fig, ax = plt.subplots()
        train_error = [run_error[error_type] for run_error in self.train_error]
        test_error = [run_error[error_type] for run_error in self.test_error]
        ax.plot(train_error, label='train')
        ax.plot(test_error, label='test')
        ax.set_xlabel("Run")
        ax.set_ylabel(f"{error_type} [%]")
        plt.show()
