import discord
from discord.ext import commands


class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Setup geladen!)
  
  @commands.command()
  async def help(self, ctx):
      with open('config/prefixes.json') as f:
        config = json.load(f)
        prefix = config(str(guild.id)
      embed=discord.Embed(description="Plasma", color=0x74a7ff)
      embed.add_field(name="Generell", value="{prefix}setup | {prefix}changeprefix | {prefix}resetprefix", 
                      inline=True)
      embed.add_field(name="Moderation", value="{prefix}ban | {prefix}unban | {prefix}kick | {prefix}mute", 
                      inline=True)
      embed.add_field(name="Automod", value="", 
                      inline=True)
      embed.add_field(name="Audit", value="", 
                      inline=True)
      embed.add_field(name="Utils", value="", 
                      inline=True)
      embed.add_field(name="Giveaway", value="", 
                      inline=True)
      await ctx.send(embed=embed)
      
def setup(client):
  client.add_cog(Help(client))