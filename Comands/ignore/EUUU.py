import json, Tasks
from random import randint
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound, CommandInvokeError
import discord

class Ofença(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """@commands.Cog.listener()
    async def on_ready(self):

        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game('MURYO KUSHO'))
        # ddd >|Help ->ajuda gg
        print(f'Estou Online, como: {self.bot.user}')

        self.Kk = []
        for i in self.bot.commands:
            self.Kk.append(str(i.name).lower())
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        F =LP.load_json('Json/Server.json')
        H = LP.load_json('Json/Players.json')

        Player = str(message.author.id)
        Server = str(message.guild.id)
        
        if not str(message.guild.id) in F:
            LP.create_json_default(Server=Server, Player=Player)

        if not Player in H[Server]:
            LP.create_player_defaukt(Server=Server, Player=Player)

                

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.reply('Favor, enviar todos os argumentos!!')
        
        elif isinstance(error, CommandNotFound):
            Command = str(error).lower().replace('" is not found', '').replace('command "', '')

            F = LP.load_json('Json/Server.json')

            if Command.lower() in F[str(ctx.guild.id)]['Commaand']['Message']:
                num = randint(0, int(len(F[str(ctx.guild.id)]['Commaand']['Message'][str(Command).lower()]['content']['Message']['content'])) - 1)

                await ctx.reply(F[str(ctx.guild.id)]['Commaand']['Message'][str(Command).lower()]['content']['Message']['content'][num])

            elif Command.lower() in F[str(ctx.guild.id)]['Commaand']['Embed']:
                Embed = discord.Embed(
                    title=str(F[str(ctx.guild.id)]['Commaand']['Embed'][Command.lower()]['title']),
                    description=str(F[str(ctx.guild.id)]['Commaand']['Embed'][Command.lower()]['description']),
                    colour=10181046
                )

                if F[str(ctx.guild.id)]['Commaand']['Embed'][Command.lower()]['image'] != None:
                    Embed.set_image(url=str(F[str(ctx.guild.id)]['Commaand']['Embed'][Command.lower()]['image']))
                    
                if F[str(ctx.guild.id)]['Commaand']['Embed'][Command.lower()]['tumb'] != None:
                    Embed.set_thumbnail(url=str(F[str(ctx.guild.id)]['Commaand']['Embed'][Command.lower()]['tumb']))

                await ctx.send(embed=Embed)
            
            return

            
        elif isinstance(error, CommandInvokeError):
            await ctx.reply(f'Tem alguma coisa errada no Código <@510948690354110464>')

        else:
            raise error

    @commands.command(name='Teste-do-Teste')
    async def _____________(self, ctx: commands.Context):
        Num = 1000000

        Num = tuple(f'{Num:,}')"""

def setup(bot):
    bot.add_cog(Ofença(bot))