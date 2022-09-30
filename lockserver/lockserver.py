import asyncio
import copy
from datetime import datetime

import discord
from discord.ext import commands

class LockServer(commands.Cog):
    """Lock the server and block everyone to send messages"""
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command(aliases=["server-lock"])
    @commands.guild_only()
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
            embed=discord.Embed(description=f"```Il server è ora bloccato per l'invio di messaggi.```", color=discord.Color.red(), timestamp=datetime.utcnow())
        else:
            await everyone.edit(permissions=perms_on, reason=f"{member.display_name} ha sbloccato il server")
            embed=discord.Embed(description=f"```Il server è ora sbloccato per l'invio di messaggi.```", color=discord.Color.green(), timestamp=datetime.utcnow())
        embed.set_author(name="|  Blocco Server", icon_url=member.avatar_url)
        embed.set_footer(text=f"Richiesto da {member.display_name}")
        await ctx.send(embed=embed)
        await ctx.message.delete()
            
async def setup(bot):
  await bot.add_cog(LockServer(bot))
