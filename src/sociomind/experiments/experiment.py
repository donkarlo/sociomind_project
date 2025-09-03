from src.sociomind.experiments.scenario import Scenario


class Experiment:
    def __init__(self, learning_scenarios:Scenario , test_scenarios: tuple[Scenario,...]):
        self._testing_scenarios = test_scenarios
        self._learning_scenarios = learning_scenarios

    def learn(self)->None:
        self._learning_scenario.learn()