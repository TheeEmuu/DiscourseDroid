from generator import newFighter
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')

@bot.command()
async def fighter(ctx):
    response = newFighter()
    await ctx.send(response)

@bot.command()
async def battle(ctx):
    response = newFighter() + " vs. " + newFighter()
    await ctx.send(response)

bot.run(TOKEN)