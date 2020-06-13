import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class TicketManagement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @group(name="ticket", invoke_without_command=True)
    @commands.has_any_role(659513332218331155, 676408167063879715, 720221658501087312)
    async def ticket(self, ctx: Context) -> None:
        """Aprire e chiudere un ticket o inviare una guida per il Supporto Vindertech."""
        await ctx.send_help(ctx.command)

    @ticket.command(name="open")
    @commands.has_any_role(659513332218331155, 676408167063879715, 720221658501087312)
    async def open(self, ctx: Context, user: discord.Member):
        """Aprire un ticket per l'utente specificato"""
        
    
    
        
def setup(bot):
    bot.add_cog(TicketManagement(bot))
