"""Test file for plugins"""

from app.plugins.discord import DiscordCommand
from app.plugins.email import EmailCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand


def test_email_command(capsys):
    """Test EmailCommand execution"""
    email_command = EmailCommand()
    email_command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "I will email you"

def test_discord_command(capsys):
    """Test DiscordCommand execution"""
    discord_command = DiscordCommand()
    discord_command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "I will send something to discord"

def test_greet_command(capsys):
    """Test GreetCommand execution"""
    greet_command = GreetCommand()
    greet_command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
    

def test_goodbye_command(capsys):
    """Test GoodbyeCommand execution"""
    goodbye_command = GoodbyeCommand()
    goodbye_command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye"

    
