import discord
import os

token = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Halo'):
        role = discord.utils.get(message.author.server.roles, name='Programmer')
        await client.add_roles(role)
        await message.channel.send('Hello!')


client.run(token)