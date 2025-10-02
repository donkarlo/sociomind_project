from typing import Optional, List

from sociomind.cli import Cli

class Main:
    def __init__(self, faked_cli_args: Optional[List[str]] = None):
        sociomind_cli = Cli(faked_cli_args)
        sociomind_cli.run()




def main(faked_cli:Optional[List[str]]=None)->None:
    main_obj:Main = Main(faked_cli)

if __name__== "__main__":
    """
    From commadn line in the venv run sociomind xpr oldest learn
    """
    faked_cli_prog_name = ["sociomind"]
    faked_cli_args = ["xpr" , "oldest" , "learn"]
    faked_cli = faked_cli_prog_name + faked_cli_args

    main(faked_cli)