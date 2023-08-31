import discord, json
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
    embed = discord.Embed(description = '{logo} Plasma\n')
    embed.add_field(name = 'Generel', value = f'`{prefix}setup` | `{prefix}help` |', inline = True)
    embed.add_field(name = 'Information', value = f'`{prefix}userinfo` | `{prefix}Serverinfo` | `{prefix}Botinfo`', inline = True)
    embed.add_field(name = 'Moderation/AutoMod', value = 'test', inline = True)
    embed.add_field(name = 'Giveaway', value = 'test', inline = True)
    await ctx.send(embed = embed)
    

async def setup(client):
  await client.add_cog(Help(client))