from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

maxLevel = 140;
levels = {};

def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [⚡" + str(i) + "]";

# Setup
setup(maxLevel);


class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        if content.isdigit():
            # Var Definition
            author  = ctx.author;
            message = ctx.message;
            ctx.send(' Content: ' + content)
            index = int(content)
            # New Nickname
            if index > 0 and index <= len(levels):
                tag = levels[index];
                author.edit(nick=author.name + tag)
                # Reaction
                message.add_reaction('✅')
            else:
                ctx.send(':warning: **Per favore inserisci un power level valido.**')
        else:
           ctx.send(':warning: **Per favore inserisci solo numeri.**')
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
