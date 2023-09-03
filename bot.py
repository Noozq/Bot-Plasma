import discord
import json
import os
import colorama
from colorama import Fore, Style
import datetime
import random
import ezcord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
from asyncio import sleep
import dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
version = str(os.getenv("VERSION"))

def get_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.launch_time = datetime.utcnow()

@client.event
async def on_ready():
    dotenv.load_dotenv()
    version = str(os.getenv("VERSION"))
    cogs = str(os.getenv("COGS"))
    print(Fore.BLUE +
    '██▓███   ██▓    ▄▄▄        ██████  ███▄ ▄███▓ ▄▄▄         ▒██   ██▒    ███▄    █  ▒█████   ▒█████  ▒███████▒  █████   \n'
    '▓██░  ██▒▓██▒   ▒████▄    ▒██    ▒ ▓██▒▀█▀ ██▒▒████▄       ▒▒ █ █ ▒░    ██ ▀█   █ ▒██▒  ██▒▒██▒  ██▒▒ ▒ ▒ ▄▀░▒██▓  ██▒\n'
    '▓██░ ██▓▒▒██░   ▒██  ▀█▄  ░ ▓██▄   ▓██    ▓██░▒██  ▀█▄     ░░  █   ░   ▓██  ▀█ ██▒▒██░  ██▒▒██░  ██▒░ ▒ ▄▀▒░ ▒██▒  ██░\n'
    '▒██▄█▓▒ ▒▒██░   ░██▄▄▄▄██   ▒   ██▒▒██    ▒██ ░██▄▄▄▄██     ░ █ █ ▒    ▓██▒  ▐▌██▒▒██   ██░▒██   ██░  ▄▀▒   ░░██  █▀ ░\n'
    '▒██▒ ░  ░░██████▒▓█   ▓██▒▒██████▒▒▒██▒   ░██▒ ▓█   ▓██▒   ▒██▒ ▒██▒   ▒██░   ▓██░░ ████▓▒░░ ████▓▒░▒███████▒░▒███▒█▄ \n'
    '▒▓▒░ ░  ░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ▒░   ░  ░ ▒▒   ▓▒█░   ▒▒ ░ ░▓ ░   ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░▒▒ ▓░▒░▒░░ ▒▒░ ▒ \n'
    '░▒ ░     ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░░  ░      ░  ▒   ▒▒ ░   ░░   ░▒ ░   ░ ░░   ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░░▒ ▒ ░ ▒ ░ ▒░  ░ \n'
    '░░         ░ ░    ░   ▒   ░  ░  ░  ░      ░     ░   ▒       ░    ░        ░   ░ ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░ ░ ░ ░   ░     \n'
    '             ░  ░     ░  ░      ░         ░         ░  ░    ░    ░              ░     ░ ░      ░ ░    ░ ░        ░    \n'
    '                                                                                              ░                       \n'
    '╭———————————————┬——————————————————┬——————————————————┬———————————————————┬——————————————┬—————————————┬——————————————╮\n'                        
    '│   Username    │    ClientID      │     Version      │      Server       │    Github    │    Owner    │     Cogs     │\n'
    '├———————————————┼——————————————————┼——————————————————┼———————————————————┼——————————————┼—————————————┼——————————————┤\n'
   f'│  {client.user}  │{client.user.id}│    {version}    │         {len(client.guilds)}         │  Bot-Plasma  │    NOOZQ    │      {cogs}      │\n'
    '╰———————————————┴——————————————————┴——————————————————┴———————————————————┴——————————————┴—————————————┴——————————————╯\n'
    )
    cogs_list = [
        'moderator',
        'setup',
        'utils',
        'owner',
        'help',
        'giveaway',
        'automod',
        'audit'
    ]

    for cog in cogs_list:
        client.load_extension(f'cogs.{cog}')
        print(f'[+] {cog} Loaded')

###################################################################
@client.event
async def on_guild_join(guild):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

  with open('config/prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

  with open('config/data/guildinfo.json', 'r') as f:
      data = json.load(f)

      data["Guildid"] = str(guild.id)
      data["Guildname"] = str(guild.name)

  with open('config/data/guildinfo.json', 'w') as f:
    json.dump(data, f, indent=4)


@client.event
async def on_guild_remove(guild):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('config/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

  with open('config/data/guildinfo.json', 'r') as f:
      data = json.load(f)

      data["Guildid"].pop(str(guild.id))
      data["Guildname"].pop(str(guild.name))

  with open('config/data/guildinfo.json', 'w') as f:
    json.dump(data, f, indent=4)

###################################################################
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

client.run(token)
