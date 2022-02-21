import discord

import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Hallo {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Max'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('ist'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('ein'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('Diker Sack'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '-help' in message.content:
        await message.channel.send('**Command`s die du verwenden kannst:**\r\n'
                                    '-help, -userinfo, -github')

client.run('')
