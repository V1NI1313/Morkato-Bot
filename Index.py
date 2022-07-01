from discord.ext import commands
from decouple import config
import os, discord


intents = discord.Intents.default()
intents.messages = True
intents.members = True

o = '!'
bot = commands.Bot(command_prefix=o, case_insensitive = True, intents=intents)

def load_cogs(bot):

    for i in os.listdir('Moder_Commands'):
        if i.endswith(".py"):
            cog = i[:-3]
            bot.load_extension(f'Moder_Commands.{cog}')

    for i in os.listdir('Comands'):
        if i.endswith(".py"):
            cog = i[:-3]
            bot.load_extension(f'Comands.{cog}')

    for i in os.listdir('Alpha Test'):
        if i.endswith(".py"):
            cog = i[:-3]
            bot.load_extension(f'Alpha Test.{cog}')

    for i in os.listdir('RP commands'):
        if i.endswith(".py"):
            cog = i[:-3]
            bot.load_extension(f'RP commands.{cog}')

    for i in os.listdir('RP commands/R'):
        if i.endswith(".py"):
            cog = i[:-3]
            bot.load_extension(f'RP commands.R.{cog}')

load_cogs(bot)

#OTYzODYyODQ4ODg5NTgxNjM4.YlcROg.PBOycD27lQjDG1N1oiz_WQeC-LU
TOKEN = config('TOKEN')
bot.run(TOKEN)