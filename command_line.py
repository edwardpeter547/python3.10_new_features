from ast import arguments
from typing import List

from click import argument
from command import Command


class CommandLine(object):
    
    def run_command(self, command: str) -> None:
        
        match command:
            case "quit":
                print("quitting the program")
                quit()
            
            case "reset":
                print("Resetting the system.")
                
            case unknown_command:
                print(f"Unkown Command: {unknown_command}")
            

    def run_command_v2(self, command: str) -> None:
        match command.split():
            case ["load", filename]:
                print(f"Loading file: {filename}")
                
            case ["save", filename]:
                print(f"Saving file: {filename}")
                
            case ["quit" | "exit" | "bye", *rest]:
                if "--force" in rest or "-f" in rest:
                    print("Sending SIGTERM to all processes and quitting the program")
                else:
                    print(f"{rest} was entered!")
                    print("Quitting the system!")
                quit()
                    
            case unknown:
                print(f"Invalid command: {command}")
            
            
    def run_command_v3(self, command):
        match command.split():
            case ["load", filename]:
                print(f"Loading: {filename}")
                
            case ["save", filename]:
                print(f"Saving: {filename}")
            
            case ["quit" | "exit" | "bye", *rest] if "--force" in rest or "-f" in rest:
                print("sending SIGTERM to all processes and quitting program")
                quit()
                
            case ["quit" | "exit" | "bye"]:
                print("Quitting the System")
                quit()
                
            case _:
                print(f"Invalid Command: {command}")
                
                
    def run_command_v4(self, command: Command) -> None:
        match command:
            case Command(command="load", arguments=[filename]):
                print(f"Loading: {filename}")
            
            case Command(command="save", arguments = [filename]):
                print(f"Saving: {filename}")
                
            case Command(command="quit" | "exit" | "bye", arguments = ["--force" | "-f", *rest]):
                print("sending SIGTERM to all processes and quitting the program")
                quit()
                
            case Command(command="quit" | "exit" | "bye"):
                print("Quitting the program")
                quit()
                
            case _:
                print(f"Unknown Comamnd: {command.command}")