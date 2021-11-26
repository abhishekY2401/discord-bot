import os
import discord
from discord import channel
from discord.flags import Intents
from discord.ext import commands, tasks
import youtube_dl

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
        f'Hello {member.name}!, Welcome to the {GUILD} 👋')


@client.event
async def on_message(message):
    if message.content.startswith('hp!greet'):
        channel = message.channel
        await channel.send('Say Hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(
            'Hello {.author}! 👋\n'
            'I am helping bot meant to help everyone. If you need any help then tag me with some of the following commands:\n'
            '👉 hp!greet\n'
            '👉 hp!qn\n'
            '👉 hp!music\n'
            'Sorry if there is a mistake, I am still under development 🙏'.
            format(msg))


client.run(TOKEN)
