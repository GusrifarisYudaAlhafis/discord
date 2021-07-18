import discord

@client.event
async def on_message(message):
    user = ctx.message.author
    if message.content.lower() == "Halo":
        await user.add_roles(discord.utils.get(user.guild.roles, name="Programmer"))




client.run(token)