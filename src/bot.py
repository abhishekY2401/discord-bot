import os
import discord
from discord.flags import Intents

from dotenv import load_dotenv

load_dotenv()
# Read an environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
# Make a client object by using the discord client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild == GUILD:
            break

    print(f'{client.user} is connected to following guild:\n'
          f'{guild.name} (id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}!, Welcome to the Dev Team 👋')


client.run(TOKEN)
