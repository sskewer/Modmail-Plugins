import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class PowerLevel(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        
@client.command()
async def powerlevel(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
