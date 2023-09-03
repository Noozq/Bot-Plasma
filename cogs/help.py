import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @discord.slash_command()
  async def help(self, ctx):
    await ctx.respond('test')

def setup(client):
  client.add_cog(Help(client))