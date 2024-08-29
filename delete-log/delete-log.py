import datetime

import discord
from discord.ext import commands


class DeleteLogPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        guild = await self.bot.fetch_guild(payload.guild_id)
        logChannel = await self.bot.fetch_channel("827832459609374730")
        embed = discord.Embed(
            color=58367, title=":wastebasket: Messaggio eliminato", timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(
            text=guild.name, icon_url=guild.icon.url if guild.icon else "https://cdn.discordapp.com/embed/avatars/0.png"
        )
        embed.add_field(name="ID Messaggio", value=f"`{payload.message_id}`", inline=True)
        if payload.cached_message:
            embed.add_field(
                name="Utente",
                value=f"<@{payload.cached_message.author.id}> \n (`{payload.cached_message.author.id}`)",
                inline=True,
            )
        embed.add_field(
            name="Canale",
            value=f"<#{payload.channel_id}> \n (`{payload.channel_id}`)",
            inline=True,
        )
        embed.add_field(name="Messaggio", value=f"`{payload.cached_message.content}`", inline=False)
        logChannel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(DeleteLogPlugin(bot))
