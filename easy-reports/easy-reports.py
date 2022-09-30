from datetime import datetime

import re
import discord
from discord.ext import commands
from discord.ext.commands import group
from discord import app_commands 


class EasyReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)  
    
    @app_commands.command(name="test")
    async def test(self, interaction: discord.Interaction) -> None:
        """Test command"""
        await interaction.response.send_message("Siete due scemi!", ephemeral=False)

        
async def setup(bot):
    await bot.add_cog(EasyReports(bot))
