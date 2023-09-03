import discord
from discord.ext import commands
from datetime import datetime, timedelta

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Setup geladen!')

    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        logo_emoji = '<:logo:1145514059320545400>'
        global emote
        latency = round(self.client.latency * 1000)
        if latency >= 0:
            if latency <= 99:
                emote = str("🟢")
            if latency >= 100:
                if latency <= 119:
                    emote = str("🟡")
            if latency >= 120:
                if latency <= 200:
                    emote = str("🔴")
        embed = discord.Embed(description=f'{logo_emoji} Plasma',
                              color=discord.Colour.blurple())
        embed.add_field(name='** 🖥 Websocket Latency**', value=f'`{emote} {latency}ms`\n', inline=True)
        embed.add_field(name='** 💾 API Latency**', value=f'`✖️`\n', inline=True)
        embed.add_field(name=f'⏳ **UPTIME**', value=f'```{days} d : {hours} h : {minutes} m : {seconds} s```\n',
                        inline=False)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Utils(client))