import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

from datetime import datetime


BaseCog = getattr(commands, "Cog", object)


class Report(BaseCog):
    """Un semplice modo per segnalare gli utenti con un comportamento scorretto"""

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    def cog_unload(self):
        self.bot.slash.teardown()


async def setup(bot):
    await bot.add_cog(Report(bot))
