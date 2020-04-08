import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class PowerLevel(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @group(name="supportrole", invoke_without_command=True)
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def supportrole(self, ctx: Context) -> None:
        await ctx.send_help(ctx.command)

    @supportrole.command(name="give")
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def givesupport(self, ctx: Context, user: discord.Member):
        role = get(user.guild.roles, id=683333884871573534)
        await user.add_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving <@&{role.id}> role")

        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
