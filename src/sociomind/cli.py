from utilix.ui.cli.cli import Cli as CliBase
from sociomind.experiment.cli import Cli as SociomindExperimentCli
from abc import ABC, abstractmethod

class Cli(CliBase):
    def run(self)-> None:
        if self._args[0] == "xpr":
            xpr_cli = SociomindExperimentCli()
            xpr_cli.run()