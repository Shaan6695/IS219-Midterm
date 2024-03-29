import logging
import sys
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, args=None):
        logging.info("Available commands:")
        print("Available commands:")
        for command_name in self.command_handler.commands:
            print(command_name)
            logging.info(command_name)
        print("Type 'exit' to exit.")