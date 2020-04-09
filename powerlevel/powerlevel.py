from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

levels = {};
def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [⚡" + str(i) + "]";

# Setup
setup(140)

class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        if content.isdigit():
            # Vars
            index  = int(content);
            guild   = ctx.message.guild;
            user_id = ctx.message.author.id;
            member  = guild.get_member(user_id)
            # Reaction
            await ctx.send(member.nick)
            await ctx.send(content)
            # New Nickname
            if index > 0 and index <= 140:
                tag = levels[index];  
                await ctx.send('Hii')
                await ctx.send(tag)
                await member.edit(nick='Ciaooo')
                await ctx.message.add_reaction('✅')
            else:
                await ctx.send(':warning: **Per favore inserisci un power level valido.**')
        else:
           await ctx.send(':warning: **Per favore inserisci solo numeri.**')
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
