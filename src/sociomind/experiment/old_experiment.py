from typing import List

from sociomind.experiment.scenario import Scenario
from robotix.experiment.experiment import Experiment as RobotixExperiment


class OldExperiment(RobotixExperiment):
    def __init__(self, learning_scenarios: List[Scenario] , test_scenarios: List[Scenario]):
        super().__init__(learning_scenarios, test_scenarios)

if __name__ == '__main__':
    ls = "salam"
    oe = OldExperiment()