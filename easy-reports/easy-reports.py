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
    
    @commands.command()
    async def test(self, ctx):
        row_of_buttons = ActionRow(
            Button(
                style=ButtonStyle.green,
                label="Green button",
                custom_id="green"
            ),
            Button(
                style=ButtonStyle.red,
                label="Red button",
                custom_id="red"
            )
        )
        msg = await ctx.send("This message has buttons", components=[row_of_buttons])
        # Wait for a button click
        def check(inter):
            return inter.author == ctx.author
        inter = await msg.wait_for_button_click(check=check)
        # Process the button click
        inter.reply(f"Button: {inter.button.label}", type=ResponseType.UpdateMessage)

        
async def setup(bot):
    await bot.add_cog(EasyReports(bot))
    
    
