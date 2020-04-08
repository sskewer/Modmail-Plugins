import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class PowerLevel(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        
    @group(name="powerlevel", invoke_without_command=True)
    @commands.has_any_role(454261607799717888)
    async def powerlevel(self, ctx: Context) -> None:
        await ctx.send_help(ctx.command)

        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
