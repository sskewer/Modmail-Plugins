import asyncio

import discord
from discord.ext import commands

class MemesPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 709741388782370846 and not message.author.bot:
            embed = None
            if message.content.lower() == "docflood":
                await message.channel.send("if")
                doc = message.guild.get_member(216316781483130880)
                embed = discord.Embed(description = f"**Con tal ironía de Italia**\n\n**EN HONOR A NUESTRO LÍDER ({doc.mention})**", timestamp = datetime.datetime.now(), color = discord.Colour.gold())
                embed.set_image(url = "https://cdn.glitch.com/ce23a52c-740e-4bfd-a0b2-8e7f838de4d2%2Fimage0.png?v=1589287037268")
                embed.set_footer(text = f"Richiesto da {message.author}")
            if message.content.lower() == "theredheat":
                theredheat = message.guild.get_member(423572109684637708)
                if message.author == theredheat:
                    embed = discord.Embed(title = "Error 404: qualcosa non va...", description = "O mio supremo maestro!\nCi inchineremo tutti alla sua presenza.", timestamp = datetime.datetime.now(), color = discord.Colour.blue())
                    embed.set_thumbnail(url = message.author.avatar_url)
                    embed.set_footer(text = "Richiesto dal Maestro Supremo")
                else:
                    embed = discord.Embed(title = "Cane con Anguria sul Capo", description = f"**Autore:** {theredheat.mention}\n**Tecnica:** Olio su Discord\n**Collocazione:** Official Fortnite Italia", timestamp = datetime.datetime.now(), color = discord.Colour.green())
                    embed.set_image(url = "https://cdn.glitch.com/ce23a52c-740e-4bfd-a0b2-8e7f838de4d2%2Fimage0.jpg?v=1589229005745")
                    embed.set_footer(text = f"Richiesto da {message.author}")
            if message.content.lower() == "mettiushyper":
                mettius = message.guild.get_member(707165674845241344)
                if message.author == mettius:
                    embed = discord.Embed(title = "Error 404: qualcosa non va...", description = "O mio supremo maestro!\nCi inchineremo tutti alla sua presenza.", timestamp = datetime.datetime.now(), color = discord.Colour.orange())
                    embed.set_thumbnail(url = message.author.avatar_url)
                    embed.set_footer(text = "Richiesto dal Maestro Supremo")
                else:
                    embed = discord.Embed(title = "La Meraviglia", description = f"**Autore:** {mettius.mention}\n**Stile:** Dolce Stil Veneto\n**Collocazione:** Official Fortnite Italia", timestamp = datetime.datetime.now(), color = discord.Colour.blue())
                    embed.set_image(url = "https://cdn.glitch.com/ce23a52c-740e-4bfd-a0b2-8e7f838de4d2%2F7bed4Gr.png?v=1589286696419")
                    embed.set_footer(text = f"Richiesto da {message.author}")
            await message.channel.send(embed = embed)
            if embed != None:
                await message.delete()
                await message.channel.send(embed = embed)

async def setup(bot):
    await bot.add_cog(MemesPlugin(bot))
