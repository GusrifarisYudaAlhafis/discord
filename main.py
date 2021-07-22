import discord
import os
from discord.utils import get

token = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if "Liash" in message.content:
        await message.author.add_roles(get(message.guild.roles, id=866027113522266192))

client.run(token)