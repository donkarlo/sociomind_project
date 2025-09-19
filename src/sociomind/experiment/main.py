from src.sociomind.experiment.old_experiment import Experiment
from src.sociomind.experiment.scenario import Scenario


class Main(Experiment):
    def __init__(self, scenarios: tuple[Scenario,...]):
        super().__init__(scenarios)