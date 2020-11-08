import asyncio
import datetime
import copy

import discord
from discord import File
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class faqCommand(commands.Cog):
    """Ottenere un collegamento diretto alla FAQ indicata"""
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        
    @commands.guild_only()
    @commands.command(aliases=["domande"])
    async def faq(self, ctx):
        
            
def setup(bot):
  bot.add_cog(faqCommand(bot))
