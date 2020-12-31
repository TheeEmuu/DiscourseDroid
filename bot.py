from generator import newFighter
from database import addData
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')

approved_users = {
    80714818876608512, #Eli
    80729915732791296, #Sean
    81932447297581056  #Brady
}

@bot.command()
async def fighter(ctx):
    response = newFighter()
    await ctx.send(response)

@bot.command()
async def battle(ctx):
    response = newFighter() + " vs. " + newFighter()
    await ctx.send(response)

@bot.command()
async def ffa(ctx, num):
    response = '```'
    for i in range(0, int(num)):
        response += newFighter() + "\n"
    response += '```'
    await ctx.send(response)

@bot.command()
async def add(ctx, type, name):
    if ctx.author.id not in approved_users:
        await ctx.send("Not approved to use this command")
    else:
        ret = addData(type, name)
        await ctx.send(ret)

bot.run(TOKEN)