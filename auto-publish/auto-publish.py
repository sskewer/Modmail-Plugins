import discord
from discord import Member, Role, TextChannel, DMChannel
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class AutoPublishPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 625752242611421214 and message.author.id == 625385492438974502:
            print("AUTOPUBLISH: Message to publish detected")
            await message.publish()
            print("AUTOPUBLISH: Message published")

def setup(bot):
    bot.add_cog(AutoPublishPlugin(bot))
