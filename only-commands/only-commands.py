import asyncio

import discord
from discord.ext import commands

class OnlyCommandsPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 1277245606645075978 and not message.author.bot and not message.author.guild_permissions.administrator:
            await message.delete()

def setup(bot):
    bot.add_cog(OnlyCommandsPlugin(bot))
