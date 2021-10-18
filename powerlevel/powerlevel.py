from discord.ext import commands
from discord.utils import get
import re

def getNick(nick:str):
  form_nick = re.sub(r'\s+\[⚡\d+\]', '', nick)
  if form_nick:
    return form_nick
  else:
    return None

# Setup
max_level = 138
allowed_channels = [702576186185875546]
 
class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        """Assegnare il livello di Potenza STW al proprio nickname.\n\n**Utilizzo**\n**`/powerlevel <livello>`** - Aggiungere il livello al proprio nickname\n**`/powerlevel reset`** - Rimuovere il livello dal proprio nickname\n\n**Esempi**\n**`/powerlevel 131`** - Nickname [\\⚡131]\n**`/powerlevel reset`** - Nickname\n\n**Accorgimenti**\n- I nickname non possono superare i 32 caratteri.\n- Utilizzare esclusivamente in <#454274882688122880>."""
        error = '**<@' + str(ctx.message.author.id) + '>, per favore inserisci un power level valido.**'
        #channel check
        if ctx.channel.id in allowed_channels:
          if content.isdigit():
              # Vars
              index = int(content)
              member  = ctx.guild.get_member(ctx.message.author.id)
              # New Nickname
              if index > 0 and index <= max_level:
                  tag = " [⚡" + str(index) + "]"
                  # New Nickname
                  original_nick = getNick(ctx.message.author.display_name)
                  await member.edit(nick=original_nick + tag)
                  # Reaction
                  await ctx.message.add_reaction('✅')
              else:
                  # Send Error Message
                  await ctx.send(error)
                  # Remove Author Message
                  await ctx.message.delete()
          elif content == 'reset':
              member = ctx.guild.get_member(ctx.message.author.id)
              # New Nickname
              original_nick = getNick(ctx.message.author.display_name)
              await member.edit(nick=original_nick)
              # Reaction
              await ctx.message.add_reaction('✅')
          else:
            # Send Error Message
            await ctx.send(error)
            # Remove Author Message
            await ctx.message.delete()
        else:
          # Remove Author Message
          await ctx.message.delete()
       
def setup(bot):
    bot.add_cog(PowerLevel(bot))
