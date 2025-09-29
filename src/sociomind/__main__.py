import sys
from sociomind.cli import Cli

class Main:
    def __init__(self):
        sociomind_cli = Cli()
        sociomind_cli.run()




def main()->None:
    Main()

if __name__== "__main__":
    """
    From commadn line in the venv run sociomind xpr oldest learn
    """
    main()