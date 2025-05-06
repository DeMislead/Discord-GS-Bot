"""
Main file.
"""
import os

from dotenv import load_dotenv

from Bot import discordBot, commands


def main():
    """
    Main entry point for the application.

    :return: None
    """
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    client = discordBot.__init__()
    commands.__init__(client)
    client.run(token)


if __name__ == '__main__':
    main()
