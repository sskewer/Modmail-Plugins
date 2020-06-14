import asyncio

import contextlib
from contextlib import suppress

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
            bot_channel = message.guild.get_channel(603955376286728226)
            embed = discord.Embed(title="**Annullare la Pubblicazione?**", color=discord.Colour.dark_red())
            embed.description = f"Il [messaggio]({message.jump_url}) sarà presto pubblicato in {message.channel.mention}.\nVuoi forzare l'annullamento dell'operazione?"
            msg = await bot_channel.send(embed=embed)
            await msg.add_reaction("❌")

            def check(payload):
                return payload.user_id != self.bot.user.id and payload.message_id == msg.id and payload.emoji.name == "❌"

            try:
                await self.bot.wait_for('raw_reaction_add', check=check, timeout=60)
                await msg.clear_reactions()
                embed = discord.Embed(title="**Pubblicazione annullata**", color=0x07b43e)
                await msg.edit(embed=embed)
                print("AUTOPUBLISH: Message not published")
            except asyncio.TimeoutError:
                with suppress(discord.errors.NotFound, discord.errors.HTTPException):
                    await message.publish()
                await msg.delete()
                print("AUTOPUBLISH: Message published")

def setup(bot):
    bot.add_cog(AutoPublishPlugin(bot))
