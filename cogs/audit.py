from datetime import datetime
import pytz
import discord
from discord.ext import commands


class Audit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name = "test", guild_id=["1136418503302324284"])
    async def setlogchannel(self, ctx):
        await ctx.respond('test')


def setup(client):
    client.add_cog(Audit(client))


