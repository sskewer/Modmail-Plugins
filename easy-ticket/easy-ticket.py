from datetime import datetime
import discord, os
from discord.ext import commands
from discord.ext.commands import Context, group
from discord.utils import get

def get_user_channel(guild: discord.Guild, user_id: int):
    user_channel = None
    for channel in guild.text_channels:
        if channel.topic == f"Ticket User ID: {str(user_id)}":
            user_channel = channel
    return user_channel


class TicketManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @group(name="ticket", invoke_without_command=True)
    @commands.has_any_role(454262524955852800, 659513332218331155, 676408167063879715, 720221658501087312)
    async def ticket(self, ctx: Context) -> None:
        """Aprire e chiudere un ticket o inviare un DM per il Supporto Vindertech."""
        await ctx.send_help(ctx.command)

    @ticket.command(name="open")
    @commands.has_any_role(454262524955852800, 659513332218331155, 676408167063879715, 720221658501087312)
    async def open(self, ctx: Context, user: discord.Member):
        """Aprire un ticket per l'utente specificato"""
        # Embed
        guild_icon = ctx.guild.icon.url if ctx.guild.icon is not None else "https://cdn.discordapp.com/embed/avatars/0.png"
        
        user_embed = discord.Embed(title="**Richiesta Supporto Accettata**", description=f"Hey <@{user.id}>, la tua richiesta è stata accettata e per questo abbiamo aperto un ticket. Un membro del team Vindertech ti risponderà il prima possibile.", color=discord.Color.green(), timestamp=datetime.utcnow())
        user_embed.set_author(name=user.name, icon_url=user.display_avatar.url)
        user_embed.add_field(name="**Domande Frequenti**", value=f"Se hai bisogno delle domande e risposte frequenti, [clicca qui](https://www.epicgames.com/help/it/fortnite-c75).", inline=False)
        user_embed.add_field(name="**Supporto Tecnico**", value=f"Se hai bisogno di aiuto in gioco, contatta l'assistenza [cliccando qui](https://www.epicgames.com/help/it/contact-us?metadata=eyJoaXN0b3J5TGlua3MiOlt7InVybCI6Ii9mb3J0bml0ZS1jNzUiLCJ0aXRsZSI6IkZvcnRuaXRlIn1dLCJjYXRlZ29yeUlkIjo3NX0%3D).", inline=False)
        user_embed.add_field(name="**Bacheca Trello**", value=f"Puoi consultare i problemi già noti ad Epic Games [cliccando qui](https://trello.com/b/zXyhyOIs/fortnite-italia-community-issues).", inline=False)
        user_embed.set_footer(text=ctx.guild.name, icon_url=guild_icon)

        log_embed = discord.Embed(title="**Richiesta Supporto Aperta**", color=discord.Color.green(), timestamp=datetime.utcnow())
        log_embed.set_author(name=user.name, icon_url=user.display_avatar.url)
        log_embed.set_footer(text=ctx.guild.name, icon_url=guild_icon)
        log_embed.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
        log_embed.add_field(name="Utente", value=f"{user.mention} | ID: {user.id}", inline=False)
        # Vars
        mod = get(ctx.guild.roles, id=454262524955852800)
        ref_vindertech = get(ctx.guild.roles, id=720221658501087312)
        vindertech = get(ctx.guild.roles, id=659513332218331155)
        category = get(ctx.guild.channels, id=683363228931194899)
        channel_log = get(ctx.guild.channels, id=721809334178414614)

        # Ticket Open
        if get_user_channel(ctx.guild, user.id) == None:
            channel = await ctx.guild.create_text_channel(f"ticket-{user.name}", category=category, topic=f"Ticket User ID: {str(user.id)}")
            await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
            await channel.set_permissions(mod, read_messages=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True)
            await channel.set_permissions(ref_vindertech, read_messages=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True)
            await channel.set_permissions(vindertech, read_messages=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True)
            await channel.set_permissions(user, read_messages=True, send_messages=True, embed_links=True, attach_files=True, read_message_history=True)
            await channel.send(embed=user_embed)
            await ctx.send(f"**Ticket aperto per {user.mention} (`{str(user.id)}`)**")
            await channel_log.send(embed=log_embed)
        else:
            await ctx.send(f"L'utente {user.mention} (`{str(user.id)}`) ha già un ticket aperto.")

    @ticket.command(name="close")
    @commands.has_any_role(454262524955852800, 659513332218331155, 676408167063879715, 720221658501087312)
    async def close(self, ctx: Context, check: discord.User, *, reason: str):
        """Chiudere un ticket per l'utente specificato"""
        user = ctx.guild.get_member(check.id)
        if user == None:
            if reason.lower() == "force":
                force_channel = get_user_channel(ctx.guild, check.id)
                # Force Close
                if force_channel == None:
                    await ctx.send(f"L'utente non possiede nessun ticket aperto da poter forzare.")
                else:
                    await force_channel.delete()
                    await ctx.send(embed=discord.Embed(description=f"Chiusura **forzata** del canale effettuata!", color=discord.Color.red()))
            else:
                await ctx.send(embed=discord.Embed(description=f"L'utente non è **membro** del server!", color=discord.Color.red()))
        else:
            # Embed
            guild_icon = ctx.guild.icon.url if ctx.guild.icon is not None else "https://cdn.discordapp.com/embed/avatars/0.png"
            
            user_embed = discord.Embed(title="**Richiesta Supporto Chiusa**", color=discord.Color.red(), timestamp=datetime.utcnow())
            user_embed.set_author(name=user.name, icon_url=user.display_avatar.url)
            user_embed.set_footer(text=ctx.guild.name, icon_url=guild_icon)
            user_embed.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
            user_embed.add_field(name="Motivazione", value=reason, inline=False)

            log_embed = discord.Embed(title="**Richiesta Supporto Chiusa**", color=discord.Color.red(), timestamp=datetime.utcnow())
            log_embed.set_author(name=user.name, icon_url=user.display_avatar.url)
            log_embed.set_footer(text=ctx.guild.name, icon_url=guild_icon)
            log_embed.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
            log_embed.add_field(name="Utente", value=f"{user.mention} | ID: {user.id}", inline=False)
            log_embed.add_field(name="Motivazione", value=reason, inline=False)
            # Vars
            user_channel = get_user_channel(ctx.guild, user.id)
            channel_log = get(ctx.guild.channels, id=721809334178414614)

            # Ticket Close
            if user_channel == None:
                await ctx.send(f"L'utente {user.mention} (`{str(user.id)}`) non possiede nessun ticket aperto.")
            else:
                with open("log.txt", "w") as f:
                    history = [message async for message in user_channel.history(limit=1000)]
                    history.reverse()
                    for msg in history:
                        if not msg.author.bot:
                            date = msg.created_at.strftime("%d/%m %H:%M:%S")
                            f.write(f"[{date}]({msg.author}) {msg.content}\n")
                await user_channel.delete()
                await ctx.send(f"**Ticket chiuso per {user.mention} (`{str(user.id)}`) con motivazione: `{reason}`**")
                await channel_log.send(embed=log_embed, file=discord.File("log.txt"))
                os.remove("log.txt")
                await user.send(embed=user_embed)

    @ticket.command(name="dm")
    @commands.has_any_role(454262524955852800, 659513332218331155, 676408167063879715, 720221658501087312)
    async def dm(self, ctx: Context, user: discord.Member, *, content: str):
        """Inviare un DM all'utente specificato"""
        # Vars
        channel_log = get(ctx.guild.channels, id=721809334178414614)
        # Embed
        guild_icon = ctx.guild.icon.url if ctx.guild.icon is not None else "https://cdn.discordapp.com/embed/avatars/0.png"
        
        user_embed = discord.Embed(title="**Notifica Richiesta Supporto**", color=discord.Color.blue(), timestamp=datetime.utcnow())
        user_embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        user_embed.set_footer(text=ctx.guild.name, icon_url=guild_icon)
        user_embed.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
        user_embed.add_field(name="Messaggio", value=content, inline=False)

        log_embed = discord.Embed(title="**Invio Messaggio DM**", color=discord.Color.blue(), timestamp=datetime.utcnow())
        log_embed.set_author(name=user.name, icon_url=user.display_avatar.url)
        log_embed.set_footer(text=ctx.guild.name, icon_url=guild_icon)
        log_embed.add_field(name="Staffer", value=f"{ctx.author.mention} | ID: {ctx.author.id}", inline=False)
        log_embed.add_field(name="Utente", value=f"{user.mention} | ID: {user.id}", inline=False)
        log_embed.add_field(name="Messaggio", value=content, inline=False)
        # DM
        try:
            await user.send(embed=user_embed)
            await ctx.send(embed=log_embed)
            await channel_log.send(embed=log_embed)
        except:
            await ctx.send(f"L'utente {user.mention} (`{str(user.id)}`) non accetta messaggi privati (DM).")


async def setup(bot):
    await bot.add_cog(TicketManagement(bot))
