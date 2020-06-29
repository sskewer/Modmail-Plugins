import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
import re
from core import checks
from core.models import PermissionLevel

class SlowMode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @group(name="slowmode", invoke_without_command=True)
    async def slowmode(self, ctx, time, channel: discord.TextChannel):
        """Impostare la slowmode del canale specificato
        Non è possibile impostare una slowmode superiore alle 6 ore
        """
        if not channel:
            channel = ctx.channel

        units = {
            "d": 86400,
            "h": 3600,
            "m": 60,
            "s": 1
        }
        seconds = 0
        match = re.findall("([0-9]+[smhd])", time)
        if not match:
            embed = discord.Embed(description="⚠ Il formato tempo utilizzato non è corretto!",color = discord.Color.orange())
            return await ctx.send(embed=embed)
        for item in match:
            seconds += int(item[:-1]) * units[item[-1]]
        if seconds > 21600:
            embed = discord.Embed(description="⚠ Non puoi impostare una slowmode superiore alle 6 ore!", color=discord.Color.orange())
            return await ctx.send(embed=embed)
        try:
            await channel.edit(slowmode_delay=seconds)
        except discord.errors.Forbidden:
            embed = discord.Embed(description="⚠ Non ho i permessi necessari per fare questo!", color=discord.Color.orange())
            return await ctx.send(embed=embed)
        embed=discord.Embed(description=f"✅ {ctx.author.mention} ha impostato la slowmode `{time}` in {channel.mention}", color=discord.Color.green())
        embed.set_author(name="Modifica Slowmode")
        embed2=discord.Embed(description=f"La slowmode per questo canale è ora **`{time}`**", color=discord.Color.red())
        embed2.set_author(name="Modifica Slowmode")
        if ctx.channel == channel:
            await channel.send(embed=embed2)
        else:
            await ctx.send(embed=embed)
            await channel.send(embed=embed2)

    @slowmode.command(name="off")
    @commands.has_any_role(454262524955852800, 454268394464870401)
    async def off(self, ctx, channel: discord.TextChannel):
        """Disattivare la slowmode in un canale"""
        if not channel:
            channel = ctx.channel
            
        seconds_off = 0
        await channel.edit(slowmode_delay=seconds_off)
        embed=discord.Embed(description=f"✅ {ctx.author.mention} ha disattivato la slowmode in {channel.mention}", color=discord.Color.green())
        embed.set_author(name="Slow Mode")
        embed2=discord.Embed(description=f"La slowmode per questo canale è ora disattivata", color=discord.Color.red())
        embed2.set_author(name="Modifica Slowmode")
        if ctx.channel == channel:
            await channel.send(embed=embed2)
        else:
            await ctx.send(embed=embed)
            await channel.send(embed=embed2)

def setup(bot):
    bot.add_cog(SlowMode(bot))
