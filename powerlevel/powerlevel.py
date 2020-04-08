import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

    
class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(self, ctx, *, member: discord.Member = None)
    async def powerlevel():
        await ctx.send('Hello')
            
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
