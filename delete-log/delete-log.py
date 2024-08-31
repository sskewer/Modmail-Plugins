import datetime, asyncio, io

import discord
from discord.ext import commands


class DeleteLogPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        if payload.cached_message:
            if payload.cached_message.author.bot:
                return

        guild = await self.bot.fetch_guild(payload.guild_id)
        logChannel = await self.bot.fetch_channel("827832459609374730")

        embed = discord.Embed(
            color=discord.Color.red(), title=":wastebasket: Messaggio eliminato", timestamp=datetime.datetime.utcnow()
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
        if len(payload.cached_message.content) < 1024:
            embed.add_field(
                name="Messaggio",
                value=payload.cached_message.content if payload.cached_message.content != "" else "`sconosciuto`",
                inline=False,
            )

        if payload.cached_message:
            deleter = None

            await asyncio.sleep(0.5)
            async for entry in guild.audit_logs(limit=4, action=discord.AuditLogAction.message_delete):
                if entry.target.id == payload.cached_message.author.id and entry.extra.channel.id == payload.channel_id:
                    deleter = entry.user.id

            if deleter:
                embed.add_field(
                    name="Eliminato Da",
                    value=f"<@{deleter}> (`{deleter}`)",
                    inline=False,
                )
        if len(payload.cached_message.content) < 1024:
            await logChannel.send(embed=embed)
        else:
            await logChannel.send(
                embed=embed, file=discord.File(io.StringIO(payload.cached_message.content), filename="content.txt")
            )


async def setup(bot):
    await bot.add_cog(DeleteLogPlugin(bot))
