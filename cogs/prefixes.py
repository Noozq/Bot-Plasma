import discord
from discord.ext import commands
import json


class Prefixes(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Prefixes geladen!')

  @commands.command(pass_context=True)
  @commands.has_permissions(administrator=True)
  async def changeprefix(self, ctx, prefix):
    with open('config/prefixes.json', 'r') as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('config/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

  @commands.command(pass_context=True)
  @commands.has_permissions(administrator=True)
  async def resetprefix(self, ctx):
    mprefix = '!'
    with open('config/prefixes.json', 'r') as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = mprefix

    with open('config/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

    await ctx.send(f'Reset to: {mprefix}')


async def setup(client):
  await client.add_cog(Prefixes(client))
