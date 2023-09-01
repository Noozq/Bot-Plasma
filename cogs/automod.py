import discord
from discord.ext import commands

class Automod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Setup geladen!')

    @commands.command()
    async def Automod(self, ctx):
        embed = discord.Embed(title='test')
        await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(Automod(client))