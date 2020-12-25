from generator import newFighter
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is alive')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "!fighter":
        response = newFighter()
        await message.channel.send(response)
    elif message.content == "!battle":
        a = newFighter()
        b = newFighter()
        await message.channel.send(a + " vs. " + b)

client.run(TOKEN)