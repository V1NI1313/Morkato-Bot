from discord.ext import commands
import discord, json, asyncio
import  LPck

class Marca(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['marca-ativar', 'marcar-despertar'])
    async def Marca(self, ctx: commands.Context, *, Marca: str=''):
        M = LPck.load_json('Json/config.json')

        if Marca in M['config']['Marcas-resp']:
            print('Pegou')

    

def setup(bot):
    bot.add_cog(Marca(bot))