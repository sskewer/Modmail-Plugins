import datetime
import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class TicketManagement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @group(name="ticket", invoke_without_command=True)
    @commands.has_any_role(659513332218331155, 676408167063879715, 720221658501087312)
    async def ticket(self, ctx: Context) -> None:
        """Aprire e chiudere un ticket o inviare un DM per il Supporto Vindertech."""
        await ctx.send_help(ctx.command)

    @ticket.command(name="open")
    @commands.has_any_role(659513332218331155, 676408167063879715, 720221658501087312)
    async def open(self, ctx: Context, user: discord.Member):
        """Aprire un ticket per l'utente specificato"""
        # Embed
        embed = discord.Embed(title="**Richiesta Supporto Accettata**", description=f"Hey <@{user.id}>, la tua richiesta è stata accettata e per questo abbiamo aperto un ticket. Un membero del team Vindertech ti risponderà il prima possibile.", color=discord.Color.green(), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.add_field(name="**F.A.Q.**", value=f"Se hai bisogno delle domande e risposte frequenti, [clicca qui](https://www.epicgames.com/help/it/fortnite-c75).", inline=False)
        embed.add_field(name="**Supporto Tecnico**", value=f"Se hai bisogno di aiuto in gioco, contatta l'assistenza [cliccando qui](https://www.epicgames.com/help/it/contact-us?metadata=eyJoaXN0b3J5TGlua3MiOlt7InVybCI6Ii9mb3J0bml0ZS1jNzUiLCJ0aXRsZSI6IkZvcnRuaXRlIn1dLCJjYXRlZ29yeUlkIjo3NX0%3D).", inline=False)
        # Vars
        userchannel = None
        mod = get(ctx.guild.roles, id=454262524955852800)
        rvindertech = get(ctx.guild.roles, id=720221658501087312)
        vindertech = get(ctx.guild.roles, id=659513332218331155)
        category = get(ctx.guild.channels, id=683363228931194899)
        # Channel Check
        for channel in ctx.guild.channels:
                if channel.topic == f"User ID: {str(user.id)}":
                        userchannel = channel
	# Ticket Open
        if userchannel == None:
                channel = await ctx.guild.create_text_channel(f"ticket-{user.name}", category=category, topic=f"User ID: {str(user.id)}")
                await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
                await channel.set_permissions(mod, read_messages=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True)
                await channel.set_permissions(rvindertech, read_messages=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True)
                await channel.set_permissions(vindertech, read_messages=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True)
                await channel.set_permissions(user, read_messages=True, send_messages=True, embed_links=True, attach_files=True)
                await channel.send(embed=embed)
                await ctx.send(f"**Ticket aperto per {user.mention} (`{str(user.id)}`)**")
        else:
                await ctx.send(f"L'utente {user.mention} (`{str(user.id)}`) ha già un ticket aperto.")
        
    @ticket.command(name="close")
    @commands.has_any_role(659513332218331155, 676408167063879715, 720221658501087312)
    async def close(self, ctx: Context, user: discord.Member, *, reason: str):
        """Chiudere un ticket per l'utente specificato"""
        # Embed
        embed2 = discord.Embed(title="**Richiesta Supporto Chiusa**", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
        embed2.set_author(name=user.name, icon_url=user.avatar_url)
        embed2.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed2.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
        embed2.add_field(name="Motivazione", value=reason, inline=False)
        # Vars
        guild = ctx.guild
        userchannel = None
        # Channel Check
        for channel in ctx.guild.channels:
                if channel.topic == f"User ID: {str(user.id)}":
                        userchannel = channel
        # Ticket Close
        if userchannel == None:
                await ctx.send(f"L'utente {user.mention} (`{str(user.id)}`) non possiede nessun ticket aperto.")
        else:
                await userchannel.delete()
                await ctx.send(f"**Ticket chiuso per {user.mention} (`{str(user.id)}`) con motivazione: `{reason}`**")
                await ctx.author.send(embed=embed2)
                
    @ticket.command(name="dm")
    @commands.has_any_role(659513332218331155, 676408167063879715, 720221658501087312)
    async def dm(self, ctx: Context, user: discord.Member, *, content: str):
        """Inviare un DM all'utente specificato"""
        # Embed
        embed3 = discord.Embed(title="**Notifica Richiesta Supporto**", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
        embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed3.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed3.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
        embed3.add_field(name="Messaggio", value=content, inline=False)
        embed4 = discord.Embed(title="**DM Inviato Correttamente**", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
        embed4.set_author(name=user.name, icon_url=user.avatar_url)
        embed4.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed4.add_field(name="Utente", value=f"{user.mention} | ID: {user.id}", inline=False)
        embed4.add_field(name="Messaggio", value=content, inline=False)
        # DM
        try:
                await user.send(embed=embed3)
                await ctx.send(embed=embed4)
        except:
                await ctx.send(f"L'utente {user.mention} (`{str(user.id)}`) non accetta messaggi privati (DM).")
        
def setup(bot):
    bot.add_cog(TicketManagement(bot))
