import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message) : # Using on_message event reference you dont need to have a prefix
    guild = message.author.guild
    if message.content.lower() == "Halo" :  # Checks if the WHOLE message is that one word, so not if that one word was part of a message
        role = discord.utils.get(guild.roles, name="Programmer") # Gets the role
        if role is not None : # makes sure role exists
            await message.author.add_roles(role)


client.run(token)