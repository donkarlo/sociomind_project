from robotix.experiment.cli import Cli as RobotixCliXpr

class Cli(RobotixCliXpr):
    def run(self):
        if self.get_type() == "oldest":
            from sociomind.experiment.kind.oldest.oldest import Oldest
            oldest_xpr = Oldest()
            if self.get_command() == "learn":
                oldest_xpr.learn()