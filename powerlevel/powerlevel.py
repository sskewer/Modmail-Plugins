from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

levels = {};
def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [:zap:" + str(i) + "]";

# Setup
setup(140)

# New Nickname
if index > 0 and index <= len(levels):
    tag = levels[index];
    print(str(index) + tag)
else:
    print(':warning: **Per favore inserisci un power level valido.**')


class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        if content.isdigit():
            # Reaction
            await ctx.message.add_reaction('✅')
            await ctx.message.add_reaction('⚡')
            await ctx.send(ctx.author.name)
            index = 1;
            # New Nickname
            if index > 0 and index <= len(levels):
                tag = levels[index];
                await ctx.author.edit(nick=ctx.author.name + tag)
            else:
                await ctx.send(':warning: **Per favore inserisci un power level valido.**')
        else:
           await ctx.send(':warning: **Per favore inserisci solo numeri.**')
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
