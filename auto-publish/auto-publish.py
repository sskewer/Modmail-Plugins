import logging

import discord
from discord.ext import commands

logger = logging.getLogger("Modmail")

from core import checks
from core.models import PermissionLevel

class AutoPublishPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.channel.id == 721755696118628402 and message.author.id == 625385492438974502:
        logger.info("Message to publish detected")
        await message.publish()
        logger.info("Message published")


def setup(bot):
    bot.add_cog(AutoPublishPlugin(bot))
