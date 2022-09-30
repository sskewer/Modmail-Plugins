from datetime import datetime

import dislash
from dislash import *

import discord
from discord.ext import commands
from discord.ext.commands import group


class EasyReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)  
    
    @dislash.guild_only()
    @slash_command(description="Says Hello")
    async def hello(self, inter):
        await inter.respond("Hello from cog!")

        
async def setup(bot):
    await bot.add_cog(EasyReports(bot))
    
    
