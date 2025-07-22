from src.sociomind.experiments.scenario import Scenario


class Experiment:
    def __init__(self, learning_scenario:Scenario , test_scenarios: list[Scenario,...]):
        self._test_scenarios = test_scenarios
        self._learning_scenario = learning_scenario