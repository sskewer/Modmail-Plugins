import discord
from discord.ext import commands

from datetime import datetime


class Report(commands.Cog):
    """Un semplice modo per segnalare gli utenti con un comportamento scorretto"""

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)


async def setup(bot):
    await bot.add_cog(Report(bot))
