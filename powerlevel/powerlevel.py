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
        if (ctx.message.channel.id == '603955376286728226'):
            await ctx.message.add_reaction('✅')
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
