import discord
import os

token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_message(message):
    guild = message.author.guild
    if message.content.startswith('$Halo'):
        role = discord.utils.get(guild.roles, name="programmer")
        if role is not None:
            await message.author.add_roles(role)


client.run(token)