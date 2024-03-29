import logging
from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self):
        logging.info("Goodbye")
        print("Goodbye")