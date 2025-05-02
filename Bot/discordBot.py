import discord
from discord.ext import commands


class ServerBot(commands.Bot):

    async def on_ready(self) -> None:
        print(f"{self.user.name} is ready")

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        print(f"Received message:\nAuthor: {message.author}\nContent: {message.content}\nChannel: {message.channel.name}")
        await self.process_commands(message)


def __init__() -> ServerBot:
    intents = discord.Intents.default()
    intents.message_content = True  # NOQA

    client: ServerBot = ServerBot(command_prefix='$', intents=intents)

    return client
