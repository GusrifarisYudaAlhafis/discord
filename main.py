import discord

@client.event
async def on_message(message): # Using on_message event reference you dont need to have a prefix
    guild = message.author.guild
    if message.content.lower() == "Halo":  # Checks if the WHOLE message is that one word, so not if that one word was part of a message
        role = discord.utils.get(guild.roles, name="Programmer") # Gets the role
        if role is not None: # makes sure role exists
            await message.author.add_roles(role) # Assigns role to the message author




client.run(token)