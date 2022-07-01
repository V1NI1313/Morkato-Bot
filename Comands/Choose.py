from discord.ext import commands
import discord, random
from discord.ext.commands.errors import CommandNotFound

class Choose(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='choose')
    async def Choose(self, ctx: commands.Context, *choose):

        self.choose = ' '.join(choose).split(sep=',')
        Kk = []

        self.ramdom = random.randint(0, int(len(self.choose))-1)
        self.resposta = self.choose[self.ramdom]

        if self.resposta[0] == ' ':
            for i in range(len(self.resposta)):
                Kk.append(self.resposta[i])

            Kk.pop(0)
            self.resposta = ''.join(Kk)

        await ctx.reply(f'**Grrr, eu escolho ** `{self.resposta}`')


def setup(bot):
    bot.add_cog(Choose(bot))