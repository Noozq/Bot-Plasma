import discord
from discord.ext import commands


def setup(client):
  client.add_cog(Help(client))