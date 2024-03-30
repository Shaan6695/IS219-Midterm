import sys
import os
import logging
import logging.config
from decimal import Decimal, InvalidOperation
import pandas as pd
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from app.plugins.discord import DiscordCommand
from app.plugins.email import EmailCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand