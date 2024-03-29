import logging
import sys
from app.commands import Command


class EmailCommand(Command):
    def execute(self):
        logging.info("I will email you")
        print(f'I will email you')