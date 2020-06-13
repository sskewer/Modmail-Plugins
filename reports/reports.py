import datetime

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class Report(commands.Cog): 
    """Un semplice modo per segnalare gli utenti con un comportamento scorretto"""
    
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command(aliases=["rchannel"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def reportchannel(self, ctx, channel: discord.TextChannel):
        """Impostare il canale delle segnalazioni"""
        await self.db.find_one_and_update({"_id": "config"}, {"$set": {"report_channel": channel.id}}, upsert=True)
        
        embed = discord.Embed(color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Configurazione Canale", value=f"Canale delle segnalazioni correttamente impostato su {channel.mention}", inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(aliases=["rmention"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def reportmention(self, ctx, *, mention: str):
        """Impostare le menzioni delle segnalazioni"""
        await self.db.find_one_and_update({"_id": "config"}, {"$set": {"report_mention": mention}}, upsert=True)
        
        embed = discord.Embed(color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Configurazioni Menzioni", value=f"Menzioni delle segnalazioni correttamente impostato su {mention}", inline=False)
        
        await ctx.send(embed=embed)

    @commands.command()
    async def report(self, ctx, user: discord.Member, *, reason: str):
        """Segnalare il comportamento scorretto di un utente"""
        config = await self.db.find_one({"_id": "config"})
        report_channel = config["report_channel"]
        setchannel = discord.utils.get(ctx.guild.channels, id=int(report_channel))
        
        try:
            report_mention = config["report_mention"]
        except KeyError:
            report_mention = ""
            
        embed = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        
        embed.add_field(name="Utente segnalato", value=f"{user.mention} | ID: {user.id}", inline=False)
        embed.add_field(name="Segnalato da:", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
        embed.add_field(name="Canale", value=ctx.channel.mention, inline=False)
        embed.add_field(name="Motivazione", value=reason, inline=False)

        await setchannel.send(report_mention, embed=embed)
        await bot.delete_message(ctx.message)
        await ctx.author.send(f"Hai segnalato con successo **{user.name}** con la seguente motivazione: `{reason}`. Grazie per la collaborazione!")
        
def setup(bot):
    bot.add_cog(Report(bot))
