import discord
from discord.ext import commands


class ServerBot(commands.Bot):
    """
    Represents a bot that inherits from the commands.Bot class.
    """

    async def on_ready(self) -> None:
        """
        Logs a message indicating the bot is ready. This method is triggered
        when the bot has successfully connected and is ready to interact with the API.

        :return: None
        """
        print(f"{self.user.name} is ready")

    async def on_message(self, message) -> None:
        """
        Handles incoming messages and processes commands if applicable.

        This method asynchronously listens for messages and allows further processing.
        It filters out messages sent by the bot itself and then logs important message-related
        details such as the author, content, and channel. If the message requires further
        processing, it invokes the command processing functionality.

        :param message: The incoming message object containing details such as the author,
            content, and channel.
        :type message: Message
        """
        if message.author == self.user:
            return

        print(f"Received message:\n"
              f"Author: {message.author}\n"
              f"Content: {message.content}\n"
              f"Channel: {message.channel.name}")

        await self.process_commands(message)


def __init__() -> ServerBot:
    """
    Initializes and returns an instance of the ServerBot client.

    This function configures the necessary intents for the bot, particularly
    enabling message content intent. It then initializes the ServerBot
    instance using the specified command prefix and the configured intents.

    :return: An instance of the ServerBot client.
    :rtype: ServerBot
    """
    intents = discord.Intents.default()
    intents.message_content = True  # NOQA

    client: ServerBot = ServerBot(command_prefix='$', intents=intents)

    return client
