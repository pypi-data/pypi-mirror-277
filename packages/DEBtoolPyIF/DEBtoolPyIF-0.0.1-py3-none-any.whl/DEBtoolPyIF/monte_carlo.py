import random

from DEBpython.pet import Pet
from code_generator import IndividualStepCodeGenerator
from matlab_wrapper import EstimationRunner

from os import mkdir
from datetime import datetime as dt


class MonteCarloEstimation:
    def __init__(self, par_bounds, folder, code_gen: IndividualStepCodeGenerator, extra_parameter_filter=None):
        self.par_bounds = par_bounds
        self.folder = folder
        self.code_gen = code_gen
        if not callable(extra_parameter_filter):
            raise Exception("Parameter filter must be callable.")
        self.extra_par_filter = extra_parameter_filter

    def gen_viable_pars(self):
        while True:
            pars = {}
            for par, bounds in self.par_bounds.items():
                if isinstance(bounds, (tuple, list)):
                    # Generate random number within bounds
                    pars[par] = random.uniform(*bounds)
                else:
                    # Copy parameter value
                    pars[par] = bounds
            if self.check_pars(pars):
                return pars

    def check_pars(self, pars):
        pet = Pet(**pars)
        valid, invalid_reason = pet.check_validity()
        if not valid:
            return False
        viable, inviable_reason = pet.check_viability()
        if not viable:
            return False
        return self.extra_par_filter(pet)

    def estimate(self, n_samples, hide_output=True):
        i = 0
        runner = EstimationRunner()
        results = {}
        while i < n_samples:
            # Generate random parameter values that pass filters
            pars = self.gen_viable_pars()

            current_time = dt.today().isoformat(sep=' ', timespec='seconds')
            estimation_folder = f"{self.folder}/{current_time.replace(':', '_')}"
            mkdir(estimation_folder)
            self.code_gen.generate_code(output_folder=estimation_folder, default_pars=pars, estimate_group_pars=True)

            results[i] = runner.run_estimation(estimation_folder, self.code_gen.species_name,
                                               window=False, clear_before=True, hide_output=hide_output)
            print(f"{current_time} |> sb {results[i]['estimation_errors']['final']['sb']:.5f} pars {pars}")