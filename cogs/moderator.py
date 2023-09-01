import discord
from discord.ext import commands

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Setup geladen!')

    @commands.command()
    async def mod(self, ctx):
        embed = discord.Embed(title='test')
        await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(Moderator(client))