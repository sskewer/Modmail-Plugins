import asyncio
import datetime
import copy

import discord
from discord import File
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class LockServer(commands.Cog):
    """Lock the server and block everyone to send messages"""
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        
    @commands.guild_only()
    @commands.command(aliases=["server-lock"])
    @commands.has_permissions(ban_members=True)
    async def lockserver(self, ctx):
        member = ctx.guild.get_member(ctx.message.author.id)
        everyone = ctx.guild.default_role
        permissions = everyone.permissions
        perms_on = copy.copy(permissions)
        perms_off = copy.copy(permissions)
        perms_on.update(send_messages=True)
        perms_off.update(send_messages=False)
        
        if permissions.send_messages == True:
            await everyone.edit(permissions=perms_off, reason=f"{member.display_name} ha bloccato il server")
            embed=discord.Embed(description=f"```Il server è ora bloccato per l'invio di messaggi.```", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
            embed.set_author(name="|  Blocco Server", icon_url=member.avatar_url)
            embed.set_footer(text=f"Richiesto da {member.display_name}")
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
            await everyone.edit(permissions=perms_on, reason=f"{member.display_name} ha sbloccato il server")
            embed2=discord.Embed(description=f"```Il server è ora sbloccato per l'invio di messaggi.```", color=discord.Color.green(), timestamp=datetime.datetime.utcnow())
            embed2.set_author(name="|  Blocco Server", icon_url=member.avatar_url)
            embed2.set_footer(text=f"Richiesto da {member.display_name}")
            await ctx.send(embed=embed2)
            await ctx.message.delete()
            
def setup(bot):
  bot.add_cog(LockServer(bot))
