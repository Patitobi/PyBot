from turtle import title
from unicodedata import name
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
    
    if 'Patitobi' in message.author.name:
        if 'Moin' in message.content:
            await message.channel.send('Moin Chef')

    if '-help' in message.content:
        await message.channel.send('**Command`s die du verwenden kannst:**\r\n'
                                    '-help\r\n'
                                    '-userinfo\r\n'
                                    '-github\r\n'
                                    '+penis\r\n'
                                    '+wixen\r\n')

    if '-github' in message.content:
        await message.channel.send('Der gesammte Code von mir ist auf github einsebar.\r\n'
                                    'Folge dem Link un den Code zu sehen:\r\n'
                                    'https://github.com/Patitobi/PyBot')
    
    if '+penis' in message.content:
        await message.channel.send('Gib es noch nicht')
        
    if '+wixen' in message.content:
        await message.channel.send('Gib es noch nicht')

    if message.content.startswith('userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member : Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='User Infos über {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen +=   '{} \r\n'.format(role.mention)      
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Valla')
                await message.channel.send(embed=embed)
                
                
                
    
client.run('OTQ1MzQ2ODYwMDc0MjgzMDE4.YhO03w.F6ZjFdZSInmcg5Vc7UpR2B7Vwok')
