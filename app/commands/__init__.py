from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class HistoryCommand(Command):
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def execute(self, *args):
        self.app_instance.display_history()

# Modify CommandHandler to handle 'history' command
class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.history = []  # Initialize history as an empty list

    def register_command(self, command_name, command_instance):
        self.commands[command_name] = command_instance

    def execute_command(self, command_name, *args):
        command_instance = self.commands.get(command_name)
        if command_instance:
            return command_instance.execute(*args)
        else:
            print(f"No such command: {command_name}")

    def add_to_history(self, calculation):
        self.history.append(calculation)  # Add calculation to history list

    def get_history(self):
        return self.history  # Return the history list