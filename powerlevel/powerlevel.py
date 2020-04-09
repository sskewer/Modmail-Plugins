from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

maxLevel = 140;
levels = {};

def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [:zap: " + str(i) + "]";

# Setup
setup(maxLevel);


class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        if content.isdigit():
            # index = int(content)
            # Var Definition
            author  = ctx.author;
            message = ctx.message;
            await ctx.send(' Content: ' + content)
            # New Nickname
            if index > 0 and index <= len(levels):
                tag = levels[index];
                await author.edit(nick=author.name + tag)
                # Reaction
                await message.add_reaction('✅')
            else:
                await ctx.send(':warning: **Per favore inserisci un power level valido.**')
        else:
           await ctx.send(':warning: **Per favore inserisci solo numeri.**')
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
