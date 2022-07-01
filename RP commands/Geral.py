import asyncio
import discord
from discord.ext import commands
from Index import o

class Geral(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['respiracao', 'resp'])
    async def Respiração(self, ctx: commands.Context, Res: str='None'):
        if Res == 'None':
            Embed = discord.Embed(
            title='Respiração',
            description='As respirações de Demon Slayer são técnicas de esgrima ensinadas por um mestre, para fazer com que os caçadores de Onis possam enfrentar todos os demônios, sejam eles fracos, semelhantes (poder) ou superiores. Como é o caso dos Lua Superiores criados por Muzan Kibutsuji.\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
            colour= 11598249
            )
        
            Embed.set_image(url='https://i.pinimg.com/originals/a3/34/6c/a3346cc151cbb8c20c57d05e83c932f3.gif')

            msg = await ctx.send(embed=Embed)

            await msg.add_reaction('🌊')
            await msg.add_reaction('☀️')
            await msg.add_reaction('💨')
            await msg.add_reaction('🌙')
            await msg.add_reaction('⚡')

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30, check=lambda r=discord.Reaction, u=discord.User: u.id == ctx.author.id)

                if str(reaction.emoji) == '🌊':
                    Res = 'agua'

                elif str(reaction.emoji) == '☀️':
                    Res = 'sol'

                elif str(reaction.emoji) == '💨':
                    Res = 'nevoa'

                elif str(reaction.emoji) == '🌙':
                    Res = 'lua'

                elif str(reaction.emoji) == '⚡':
                    Res = 'trovao'
                
                await msg.delete()

            except asyncio.TimeoutError:
                pass

        if Res.lower().replace('á', 'a') == 'agua':
            Embed = discord.Embed(
                    title='Respiração-da-Água',
                    description='Sendo a primeira Respiração apresenta em Demon Slayer: Kimetsu no Yaiba, a Respiração da Água é dita como a mais comum entre os Caçadores de Demônios, por possuir uma variedade de técnicas maior e por teoricamente ser a mais “fácil” dos novatos dominarem.\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
                    colour= 2123412
                )
                
            Embed.set_image(url='https://c.tenor.com/L9i_nFA3sKoAAAAC/tomioka-giyuu-demon-slayer.gif')
            Embed.add_field(name=f'Comandos da Respiração da Água\n______', value=f'**Primeira Forma**: {o}Minamo-giri\n**Segunda Forma**: {o}Mizu-guruma\n**Terceira Forma**: {o}Ryuryu-mai\n**Quarta Forma**: {o}Uchishioi\n**Quinta Forma**: {o}Kanten-no-jiu\n**Sexta Forma**: {o}Nejire-uzu\n**Sétima Forma**: {o}Shizuku-wa-Mondzuki\n**Oitava Forma**: {o}Takitsubo\n**Nona Forma**: {o}Suiryu-shibuki\n**Décima Forma**: {o}Seisei-ruten\n**Décima Primeira Forma**: {o}Nagi', inline=False)

        elif Res.lower() == 'sol':
            Embed = discord.Embed(
                    title='Respiração-do-Sol',
                    description='A dança do Deus do Fogo (ou Respiração do Sol) em Kimetsu no Yaiba: Demon Slayer, também conhecida como Hinokami Kagura, é uma técnica de respiração que apenas a família Kamado é capaz de realizar.\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
                    colour= 15844367
                )

            Embed.set_image(url='https://c.tenor.com/t99Es4AlS8IAAAAC/tanjiro-primeiro-sol.gif')
            Embed.add_field(name='Comandos da Respiração do Sol\n______', value=f'**Primeira Forma**: {o}enbu-issen\n**Segunda Forma**: {o}heki-ra\n**Terceira Forma**: {o}retsujitsu-kokyo\n**Quarta Forma**: {o}gen-nichi\n**Quinta Forma**: {o}Kasha \n**Sexta Forma**: {o}shakkotsu\n**Sétima Forma**: {o}yokatotsu\n**Oitava Forma**: {o}hirin-kagero\n**Nona Forma**: {o}shayou-tenshin\n**Décima Forma**: {o}onko\n**Décima Primeira Forma**: {o}nichiun-ryu\n**Décima Segunda Forma**: {o}homura-mai\n**Décima Terceira Forma**: {o}fenix', inline=False)

        elif Res.lower().replace('é', 'e') == 'nevoa':
            Embed = discord.Embed(
                    title='Respiração-da-Névoa',
                    description='A Respiração do Névoa é Uma Das Formas De Ataque Em Kimetsu no Yaiba – Demon Slayer. Usada Pelo Hashira Muichiro Tokito, Ela é Derivada Da Respiração do Vento.\nQuase todos os ataques desta respiração consistem em usar ataques rápidos e movimentos ocultos, para confundir e desorientar o adversário.\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
                    colour= 16777215
                ) # 16777215

            Embed.set_image(url='https://c.tenor.com/auhkPgLiYC0AAAAC/muichiro-tokito.gif')
            Embed.add_field(name='Comandos da Respiração da Névoa\n______', value=f'**Primeira Forma**: {o}Suiten-Togasumi\n**Segunda Forma**: {o}Yaekasumi\n**Terceira Forma**: {o}Kasan-Shibuki\n**Quarta Forma**: {o}Iryugiri\n**Quinta Forma**: {o}Kaun-Umi\n**Sexta Forma**: {o}Tsuki-Kasho\n**Sétima Forma**: {o}Oboro', inline=False)

        elif Res.lower() == 'lua':
            Embed = discord.Embed(
                    title='Respiração-da-Lua',
                    description='Em Demon Slayer, o principal poder dos Caçadores de Demônios está nas Respirações e suas formas, e a respiração da Lua (ou Respiração Lunar) é uma das mais poderosas delas.\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
                    colour= 7419530
                )

            Embed.set_image(url='https://c.tenor.com/tIw-WkS4ewcAAAAC/kokushibou-demon-lsayer.gif')
            Embed.add_field(name='Comandos da Respiração da Lua\n______', value=f'**Primeira Forma**: {o}Yoi-no-Miya\n**Segunda Forma**: {o}Rogetsu\n**Terceira Forma**: {o}Tsugari\n**Quinta Forma**: {o}Geppaku-Saika\n**Sexta Forma**: {o}Muken\n**Sétima Forma**: {o}Zukibae\n**Oitava Forma**: {o}Getsuryu-Rinbi\n**Nona Forma**: {o}Kudaritsuki\n**Décima Forma**: {o}Senmenzan\n**Décima Quarta Forma**: {o}Kyohen\n**Décima Sexta Forma**: {o}Gekko', inline=False)

        elif Res.lower().replace('ã', 'a') == 'trovao':
            Embed = discord.Embed(
                title='Respiração-do-Trovão',
                description='Utilizada por Zenitsu, a Respiração do Relâmpago (Trovão) é um dos principais Estilos de Respiração de Demon Slayer, sendo focada em golpes rápidos, com os seus usuários utilizando bastante à força das suas pernas.',
                colour=0x9B59B6
            )

            Embed.add_field(name='Comandos da Respiração do Trovão\n______', value=f'**Primeira Forma**: {o}Hekireki-Issen\n**Segunda Forma**: {o}Inadama\n**Terceira Forma**: {o}Shubun-seirai\n**Quarta Forma**: {o}Enrai\n**Quinta Forma**: {o}Netsu-kairai\n**Sexta Forma**: {o}Dengou-raigou\n**Sétima Forma**: {o}Kami')

        await ctx.send(embed=Embed)


def setup(bot):
    bot.add_cog(Geral(bot))