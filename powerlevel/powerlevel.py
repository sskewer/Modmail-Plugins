import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

levels = {'1': ' [:zap: 1]',
          '2': ' [:zap: 2]',
          '3': ' [:zap: 3]',
          '4': ' [:zap: 4]',
          '5': ' [:zap: 5]'}

    await ctx.author.edit(nick=ctx.author.display_name + levels[content])


class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        if content.isdigit():
           await ctx.message.add_reaction('✅')
           await ctx.author.edit(nick=ctx.author.display_name + levels[content])
        else:
           await ctx.send(':warning: **Per favore inserisci solo numeri.**')
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
