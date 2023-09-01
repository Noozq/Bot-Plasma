import discord
from discord.ext import commands

class Audit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Setup geladen!')

    @commands.command()
    async def audit(self, ctx):
        embed = discord.Embed(title='test')
        await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(Audit(client))