from http import client

import discord

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hallo')
  

bot.run('')