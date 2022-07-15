"""
Example application showing Python 3.10 structural pattern matching
"""
from click import argument
from command import Command
from command_line import CommandLine
import shlex


def main() -> None:
    """Main Function"""
    
    commandline = CommandLine()
    
    while True:
        command, *arguments = shlex.split(input("$ "))
        commandline.run_command_v4(Command(command=command, arguments=arguments))
        
        

if __name__ == "__main__":
    main()