from typing import List

from robotix.experiment.scenario import Scenario
from robotix.experiment.experiment import Experiment as RobotixExperiment
from sociomind.experiment.scenario.normal import Normal


class Oldest(RobotixExperiment):
    def __init__(self):
        print("I have reached oldest experiment")
        learning_scenarios = [Normal()]
        test_scenarios = [Normal()]
        super().__init__(learning_scenarios, test_scenarios)
