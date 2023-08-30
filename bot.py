import discord
import json
import os
import datetime
import random
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
from asyncio import sleep


with open('config/token.json') as f:
  data1 = json.load(f)
  token = data1["TOKEN"]

  
with open('config/version.json') as f:
  config = json.load(f)
  version = config["VERSION"]


def get_prefix(client, message):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)


@client.event
async def on_ready():
  print('=================================================')
  print(f'Botname: {client.user} • Botid: {client.user.id}')
  print('=================================================')
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await client.load_extension(f"cogs.{filename[:-3]}")
      print(f'Cogs geladen')


@client.event
async def on_guild_join(guild):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

  with open('config/prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('config/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)


@client.command()
@commands.is_owner()
async def load(ctx, *, moduls: str):
  """LOAD COMMAND"""
  await client.load_extension(f'commands.{moduls}')
  embed = discord.Embed(
      description=
      f'<:emoji_3:1144844455850029128> | **filename:** `commands.{moduls}`\n')
  embed.set_author(
      name=client.user.name,
      icon_url=
      'https://cdn.discordapp.com/attachments/1136418508029300757/1144833877957951539/IMG_2504.jpg'
  )
  embed.set_footer(text=f'{ctx.author.name}')
  await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def unload(ctx, *, moduls: str):
  """UNLOAD COMMAND"""
  await client.unload_extension(f'commands.{moduls}')
  embed = discord.Embed(
      description=
      f'<:emoji_2:1144844439748100197> | **filename:** `cogs.{moduls}`\n')
  embed.set_author(
      name=client.user.name,
      icon_url=
      'https://cdn.discordapp.com/attachments/1136418508029300757/1144833877957951539/IMG_2504.jpg'
  )
  embed.set_footer(text=f'{ctx.author.name}')
  await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def reload(ctx, *, moduls: str):
  """RELOAD COMMAND"""
  await client.reload_extension(f'commands.{moduls}')
  embed = discord.Embed(
      description=
      f'<:emoji_1:1144844416910114939> | **filename:** `cogs.{moduls}`\n')
  embed.set_author(
      name=client.user.name,
      icon_url=
      'https://cdn.discordapp.com/attachments/1136418508029300757/1144833877957951539/IMG_2504.jpg'
  )
  embed.set_footer(text=f'{ctx.author.name}')
  await ctx.send(embed=embed)


@client.command(aliases=['adminhelp', 'adminh'])
@commands.is_owner()
async def Adminhelp(ctx):
  """ADMIN PANNEL"""
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)
  prefix = prefixes[str(ctx.guild.id)]
  embed = discord.Embed()
  embed.set_author(
      name=client.user.name,
      icon_url=
      'https://cdn.discordapp.com/attachments/1136418508029300757/1144833877957951539/IMG_2504.jpg'
  )
  embed.add_field(name='Cogs:',
                  value=f'`{prefix}load <filename>`\n'
                  f'`{prefix}unload <filename>`\n'
                  f'`{prefix}reload <filename>`\n',
                  inline=True)
  embed.add_field(name='Allgemein:',
                  value=f'`{prefix}setup`\n'
                  f'`{prefix}help`\n'
                  f'`{prefix}admin-pannel`\n'
                  f'`{prefix}bot-info`',
                  inline=True)
  embed.add_field(name='Infos:',
                  value=f'Servername: `{ctx.guild.name}`\n'
                  f'Prefix: `{prefix}`\n',
                  inline=True)
  embed.set_footer(text=f'{ctx.author.name}')
  await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
  global emote
  latency = round(client.latency * 1000)
  if latency >= 0:
    if latency <= 99:
      emote = str("<:ping3:1145090054549671936>")
    if latency >= 100:
      if latency <= 119:
        emote = str("<:ping2:1145090055803777136>")
    if latency >= 120:
      if latency <= 200:
        emote = str("<:ping1:1145090028209459240>")
  embed = discord.Embed(description=f'{emote} Ping ist: {latency}ms',
                        color=discord.Colour.gold())
  embed.set_author(
      name=client.user.name,
      icon_url=
      'https://cdn.discordapp.com/attachments/1136418508029300757/1144833877957951539/IMG_2504.jpg'
  )
  await ctx.send(embed=embed)


client.run(token)
