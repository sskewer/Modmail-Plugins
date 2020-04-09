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
 
class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        # Vars
        message = ctx.message;
        guild   = message.guild;
        author  = message.author;
        user_id = author.id;
        channel = ctx.channel;
        error   = '**<@' + str(user_id) + '>, per favore inserisci un power level valido.**';
        # Check
        if channel.id == 454274882688122880 or channel.id == 454274841047072768:
          if content.isdigit():
              # Vars
              index  = int(content);
              member  = guild.get_member(user_id)
              # New Nickname
              if index > 0 and index <= 140:
                  tag = levels[index];
                  # New Nickname
                  await member.edit(nick=author.name + ' ' + tag)
                  # Reaction
                  await ctx.message.add_reaction('✅')
              else:
                  # Send Message
                  await ctx.send(error)
                  # Remove Author Message
                  await message.delete()
          elif content == 'reset':
              member  = guild.get_member(user_id)
              # New Nickname
              await member.edit(nick=author.name)
              # Reaction
              await ctx.message.add_reaction('✅')
          else:
            await ctx.send(error)
            # Remove Author Message
            await message.delete()
        else:
          # Remove Author Message
          await message.delete()
       
def setup(bot):
    bot.add_cog(PowerLevel(bot))
