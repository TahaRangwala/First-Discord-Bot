import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(token)