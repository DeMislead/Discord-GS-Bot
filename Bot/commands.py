"""
All commands for the bot.
"""
from discord.ext.commands import Context
from Bot.discordBot import ServerBot

import server


def __init__(client: ServerBot) -> None:
    """
    Initializes the bot with specified commands for interacting with the server.

    The bot supports the following commands:
    - `hello`: Sends a greeting message mentioning the user.
    - `clear`: Deletes the current channel and recreates it as a new one.
    - `start`: Starts a server application with the specified arguments.
    - `status`: Checks and sends the status of the server application.

    :param client: Instance of the ServerBot used to register commands.
    :type client: ServerBot
    """
    @client.command()
    async def hello(ctx: Context) -> None:
        await ctx.channel.send(f'hello there {ctx.author.mention}')

    @client.command()
    async def clear(ctx: Context) -> None:
        await ctx.channel.delete()
        new_channel = await ctx.channel.clone(reason="Channel was purged")
        await new_channel.edit(position=ctx.channel.position)
        await new_channel.send("Channel was purged")

    @client.command()
    async def start(ctx: Context, args) -> None:
        try:
            server.start_application(args)
            await ctx.channel.send(server.on_started(args))
        except FileNotFoundError:
            await ctx.channel.send("There is no such server")


    @client.command()
    async def status(ctx: Context, args) -> None:
        status_message = server.check_status(args)
        await ctx.channel.send(status_message)
