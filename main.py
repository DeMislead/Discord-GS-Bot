import discord
from pathlib import Path
from discord.ext import commands
import server

TOKEN = Path('.access').read_text()
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print('bot ready')
    
@client.event
async def on_message(message):
    #channel = client.get_channel(1204128463871680545)
    #await channel.send('testing')
    print(message.author, message.content, message.channel.id)
    await client.process_commands(message)
    #pass


@client.command()
async def hello(ctx):
    await ctx.channel.send(f'hello there {ctx.author.mention}')

@client.command()
async def clear(ctx):
    await ctx.channel.delete()
    new_channel = await ctx.channel.clone(reason="Channel was purged")
    await new_channel.edit(position=ctx.channel.position)
    await new_channel.send("Channel was purged")
    
@client.command()
async def start(ctx, args):
    server.start_application(args)
    await ctx.channel.send(server.onstarted(args))

@client.command()
async def status(ctx, args):
    statusMessage = server.check_status(args)
    await ctx.channel.send(statusMessage)
    
client.run(TOKEN)