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
  data = json.load(f)
  token = data["TOKEN"]

  
with open('config/version.json') as f:
  config = json.load(f)
  version = config["VERSION"]


def get_prefix(client, message):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command('help')
client.launch_time = datetime.utcnow()

outputFile = open('config/error.log', 'w')

def printing(text):
    print(text)
    if outputFile:
        outputFile.write(str(text))
      
@client.event
async def on_ready():
  print(
'██████╗░██╗░░░░░░█████╗░░██████╗███╗░░░███╗░█████╗░\n'
'██╔══██╗██║░░░░░██╔══██╗██╔════╝████╗░████║██╔══██╗\n'
'██████╔╝██║░░░░░███████║╚█████╗░██╔████╔██║███████║\n'
'██╔═══╝░██║░░░░░██╔══██║░╚═══██╗██║╚██╔╝██║██╔══██║\n'
'██║░░░░░███████╗██║░░██║██████╔╝██║░╚═╝░██║██║░░██║\n'
'╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝\n'
  )  
  with open('config/version.json') as f:
    config = json.load(f)
    app_info = await client.application_info()
    print(f'Username: {client.user}\nClientID: {client.user.id}\nVersion: {version}\nApi: {client.application.id}\nServer: {len(client.guilds)}\nApp: {app_info.name}\n')
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await client.load_extension(f"cogs.{filename[:-3]}")
      
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

@client.command()
async def uptime(ctx):
  delta_uptime = datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  logo_emoji = '<:logo:1145514059320545400>'
  global emote
  latency = round(client.latency * 1000)
  if latency >= 0:
    if latency <= 99:
      emote = str("🟢")
    if latency >= 100:
      if latency <= 119:
        emote = str("🟡")
    if latency >= 120:
      if latency <= 200:
        emote = str("🔴")
  embed = discord.Embed(description=f'{logo_emoji} Plasma',
                        color=discord.Colour.blurple())
  embed.add_field(name = '** 🖥 Websocket Latency**', value = f'`{emote} {latency}ms`\n', inline = True)
  embed.add_field(name = '** 💾 API Latency**', value = f'`✖️`\n', inline = True)
  embed.add_field(name = f'⏳ **UPTIME**', value = f'```{days} d : {hours} h : {minutes} m : {seconds} s```\n', inline = False)
  await ctx.send(embed=embed)


client.run(token)
