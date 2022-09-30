import dislash
from dislash import *

from datetime import datetime

import re
import discord
from discord.ext import commands
from discord.ext.commands import group


class EasyReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)        
        
    def cog_unload(self):
        self.bot.slash.teardown()

async def setup(bot):
    await bot.add_cog(EasyReports(bot))
    
    if not hasattr(bot, "slash"):
        bot.slash = SlashClient(bot)
