from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get
import re

# Ebic Functions
levels = {};
def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [⚡" + str(i) + "]";
 
def getNick(nick:str):
  form_nick = re.sub(r'\s+\[⚡\d+\]', '', nick)
  if form_nick:
    return form_nick;
  else:
    return None;
 
# Setup
setup(140)
 
class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        """Assegnare il livello di Potenza STW al proprio nickname.\n\n**Utilizzo**\n**`/powerlevel <livello>`** - Aggiungere il livello al proprio nickname\n**`/powerlevel reset`** - Rimuovere il livello dal proprio nickname\n\n**Esempi**\n**`/powerlevel 140`** - Nickname [\\⚡140]\n**`/powerlevel reset`** - Nickname\n\n**Accorgimenti**\n- I nickname non possono superare i 32 caratteri.\n- Utilizzare  in <#454261608324268063>, <#454274841047072768> o <#454274882688122880>."""
        # Vars
        message = ctx.message;
        guild   = message.guild;
        author  = message.author;
        user_id = author.id;
        channel = ctx.channel;
        error   = '**<@' + str(user_id) + '>, per favore inserisci un power level valido.**';
        # Check
        if channel.id == 454261608324268063 or channel.id == 454274882688122880 or channel.id == 454274841047072768 or channel.id == 454268474534133762:
          if content.isdigit():
              # Vars
              index  = int(content);
              member  = guild.get_member(user_id)
              # New Nickname
              if index > 0 and index <= 140:
                  tag = levels[index];
                  # New Nickname
                  original_nick = getNick(author.display_name)
                  await member.edit(nick=original_nick + tag)
                  # Reaction
                  await ctx.message.add_reaction('✅')
              else:
                  # Send Error Message
                  await ctx.send(error)
                  # Remove Author Message
                  await message.delete()
          elif content == 'reset':
              member  = guild.get_member(user_id)
              # New Nickname
              original_nick = getNick(author.display_name)
              await member.edit(nick=original_nick)
              # Reaction
              await ctx.message.add_reaction('✅')
          else:
            # Send Error Message
            await ctx.send(error)
            # Remove Author Message
            await message.delete()
        else:
          # Remove Author Message
          await message.delete()
       
def setup(bot):
    bot.add_cog(PowerLevel(bot))
