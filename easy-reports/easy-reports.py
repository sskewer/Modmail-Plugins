from datetime import datetime

import re
import discord
from discord.ext import commands
from discord.ext.commands import group
from discord import app_commands 


class EasyReports(commands.Cog):
    def __init__(self, bot):
        super().__init__(intents = discord.Intents.default())
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)        

    @bot.slash_command(name="test", guild_ids=[454261607799717888])
    async def test(ctx): 
        await ctx.respond("You executed the slash command!") 

        
async def setup(bot):
    await bot.add_cog(EasyReports(bot))
