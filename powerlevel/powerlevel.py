import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

    
class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def powerlevel(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if (ctx.channel.id == '603955376286728226'):
            await ctx.send('Hello')
        else:
            await ctx.send('Bye')
            
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
