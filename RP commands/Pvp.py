import discord
from discord.ext import commands

class PVP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#Humanos#
    @commands.command(name='Corte-Nichirin')
    async def C(self, ctx: commands.Context, Cor: str=None):
        self.Embed = discord.Embed(
            title='Corte Nichirin',
            description=f'Você Usou Fez um Corte usando a Nichirin\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯✦**',
            colour=15158332
        )

        if Cor == None:
            self.Embed.add_field(name='Corte Nichirin Comum\n_______', value='•「❤️ 」**1k** De Dano\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://c.tenor.com/wtlDk3glPlEAAAAC/sm32-murata.gif')

        elif Cor.lower() == 'azul':
            self.Embed.add_field(name='Corte Nichirin Azul\n______', value='•「❤️ 」**2k** De Dano **(3k Na Respiração da água)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://i.pinimg.com/originals/e1/5b/4d/e15b4dcb63fbbb2d1977ea2da5b70384.gif')

        elif Cor.lower() == 'branca':
            self.Embed.add_field(name='Corte Nichirin Branca\n______', value='•「❤️ 」**2k** De Dano**(3k Na Respiração da Névoa)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://c.tenor.com/o1n4HN3HNBQAAAAd/muichiro-tokito.gif')

        elif Cor.lower() == 'dourada':
            self.Embed.add_field(name='Corte Nichirin Dourada\n______', value='•「❤️ 」**2k** De Dano **(3k Na Respiração do Trvão)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://i.pinimg.com/originals/1d/3d/bf/1d3dbf048330590da90564fc6404451a.gif')

        elif Cor.lower() == 'verde':
            self.Embed.add_field(name='Corte Nichirin Vede\n______', value='•「❤️ 」**2k** De Dano **(3k Na Respiração do Vento)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://i.pinimg.com/originals/fa/6c/c8/fa6cc86d4e7d7d98241ea5ee1a6dd273.gif')

        elif Cor.lower() == 'roxa':
            self.Embed.add_field(name='Corte Nichirin Roxa\n______', value='•「❤️ 」**2k** De Dano **(3k Na Respiração da Lua)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://c.tenor.com/tIw-WkS4ewcAAAAC/kokushibou-demon-lsayer.gif')

        elif Cor.lower() == 'vermelha':
            self.Embed.add_field(name='Corte Nichirin Vermelha\n______', value='•「❤️ 」**3k** De Dano **(5k Na Respiração das Chamas)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://i.pinimg.com/originals/dd/7e/8e/dd7e8ed29b4377aacc482c5c75609d05.gif')

        elif Cor.lower() == 'preta':
            self.Embed.add_field(name='Corte Nichirin Preta\n______', value='•「❤️ 」**3k** De Dano **(5k Na Respiração do Sol e da Água)**\n•「💨」**250** De Fôlego', inline=False)

            self.Embed.set_image(url='https://i.pinimg.com/originals/8d/26/12/8d26127a6bf364b439b48c0baf618dce.gif')            

        elif Cor.lower() in ['carmezin', 'carmesin']:
            self.Embed.add_field(name='Corte Nichirin Carmezin\n______', value='•「❤️ 」**5k** De Dano **(5k Na Respiração do Sol e da Água)**\n•「💨」**500** De Fôlego', inline=False)

            self.Embed.set_image(url='https://c.tenor.com/h-FsXLaDDWMAAAAC/yoruichi-demon-slayer.gif')            

        await ctx.send(embed=self.Embed)

        
 #Onis#
    @commands.command(name='Soco-oni')
    async def Corte_Nichi(self, ctx):

        await ctx.reply('✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦\n\n **Usou: Soco Oni**\n\n•「❤️」**1000** De Dano\n•「🩸」**150** De Sangue.\n\n✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦\n**Da um soco sendo um Oni no Inimigo**', file=discord.File('gif/Akaza1.gif'))

def setup(bot):
    bot.add_cog(PVP(bot))