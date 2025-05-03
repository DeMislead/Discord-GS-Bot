from discord.ext.commands import Context
from Bot.discordBot import ServerBot

import server


def __init__(client: ServerBot) -> None:
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
        statusMessage = server.check_status(args)
        await ctx.channel.send(statusMessage)
