import discord
from discord.ext import commands


class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Setup geladen!')

  @commands.command()
  async def help(self, ctx, args=None):
      help_embed = discord.Embed(title="My Bot's Help!")
      command_names_list = [x.name for x in self.client.commands]

      # If there are no arguments, just list the commands:
      if not args:
        help_embed.add_field(
          name="List of supported commands:",
          value="\n".join([str(i + 1) + ". " + x.name for i, x in enumerate(self.client.commands)]),
          inline=False
        )
        help_embed.add_field(
          name="Details",
          value="Type `.help <command name>` for more details about each command.",
          inline=False
        )

      # If the argument is a command, get the help text from that command:
      elif args in command_names_list:
        help_embed.add_field(
          name=args,
          value=self.client.get_command(args).help
        )

      # If someone is just trolling:
      else:
        help_embed.add_field(
          name="Nope.",
          value="Don't think I got that command, boss!"
        )

      await ctx.send(embed=help_embed)

def setup(client):
  client.add_cog(Help(client))