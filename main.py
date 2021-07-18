import discord
import os

token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_message(message):
    guild = message.author.guild
    if message.content.lower() == "Halo":  # Checks if the WHOLE message is that one word, so not if that one word was part of a message
        role = discord.utils.get(message.guild.roles, name="Programmer") # Gets the role
        if role is not None: # makes sure role exists
            await message.author.add_role(role) # Assigns role to the message author



client.run(token)