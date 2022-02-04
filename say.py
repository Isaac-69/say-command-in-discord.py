# importing modules
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ['!'])
"""here what the allowed_mentions will do is prevent @everyone ping and @roles ping.  
This is very helpful to prevent raids!"""

#making the status for the bot

@bot.event
async def on_ready():
    print('https://github.com/Isaac-69/say-command-in-discord.py.git') #you can remove this line lol
    print(f"{bot.user} is alive")

#creating the say cmd
@bot.command()
async def say(ctx,*, content):
    allowed_mentions = discord.AllowedMentions(everyone=False, roles=False) 
    """here what the allowed_mentions will do is prevent the bot to do @everyone ping and @roles ping even if it has perms.  
     This is very helpful to prevent raids!"""
    try:
        await ctx.message.delete()
    except Exception:
        pass
    await ctx.send(content, allowed_mentions=allowed_mentions)

bot.run(TOKEN)
