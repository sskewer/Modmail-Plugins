from datetime import datetime

import discord
from discord.ext import commands
from discord.ext.commands import group
import re

class EasyReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(EasyReports(bot))
