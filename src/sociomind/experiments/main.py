from src.sociomind.experiments.experiment import Experiment
from src.sociomind.experiments.scenario import Scenario


class Main(Experiment):
    def __init__(self, scenarios: tuple[Scenario,...]):
        super().__init__(scenarios)