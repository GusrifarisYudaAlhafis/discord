import discord
import os

token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_message(message):
    user = message.author
    if message.content.lower() == "Halo":
        role = discord.utils.get(user.guild.roles, name="Programmer")
        if role is not None:
            await user.add_roles(role)



client.run(token)