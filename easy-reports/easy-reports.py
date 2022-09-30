from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import group


class EasyReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)  
    
    @commands.Cog.listener()
    async def on_ready(self):
        synced = await self.bot.tree.sync()
        print(f'[easy-reports] INFO: Synced {len(synced)} commands')
        
    
    @app_commands.command()
    async def ping(self, interaction: discord.Interaction) -> None:
        ping1 = f"{str(round(self.bot.latency * 1000))} ms"
        embed = discord.Embed(title = "**Pong!**", description = "**" + ping1 + "**", color = 0xafdafc)
        await interaction.response.send_message(embed = embed)

        
async def setup(bot):
    await bot.add_cog(EasyReports(bot))
    
    
