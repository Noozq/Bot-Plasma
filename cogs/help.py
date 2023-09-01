import discord, json, ezcord
from discord.ext import commands

class Help(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print('lod')
  
  @commands.command()
  async def help(self, ctx):
    with open('config/prefixes.json', 'r') as f: 
      prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]

async def setup(client):
  await client.add_cog(Help(client))