import asyncio
import json
import discord, LPck
from discord.ext import commands
import RPG

class Água(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.verification = [974035102516527194]
        self.Humano = [971804637315350558]
        self.Oni = [971804639232143370]
        self.Híbrido = [971804640050040892]

    @commands.command(name='Minamo-giri')
    async def Minamo_giri(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1, 
                Nome_Forma="Minamo Giri", Geral="Embora não tenha sido a primeira técnica que vimos Tanjiro utilizar na obra, a Primeira Forma da Respiração da Água é um movimento relativamente simples, em que o espadachim impulsiona sua espada para frente realizando um poderoso corte lateral.", 
                Forma="Primeira Forma", 
                Dano="2.1k", 
                Fôlego="800", 
                url="https://nerdhits.com.br/wp-content/uploads/2021/04/primeira-forma-da-agua.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Mizu-Guruma')
    async def Mizu_Guruma(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Mizu Guruma",
                Geral="Ainda durante o teste para a entrada na Corporação dos Caçadores de Demônios, Tanjiro utilizou a Segunda Forma da Respiração da Água, em que ele salta e gira verticalmente no ar com a sua espada liberando um ataque em movimento circular.",
                Forma="Segunda Forma",
                Dano="2.7k",
                Fôlego="1.1k",
                url="https://criticalhits.com.br/anime/conheca-as-11-formas-da-respiracao-da-agua-de-demon-slayer/attachment/2-second-form-water-wheel/",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )
        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Ryuryu-Mai')
    async def Ryuryu_Mai(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Ryuryu Mai",
                Geral="Para lidar com a combinação dos ataques dos demônios Yahaba e Susamaru, Tanjiro utilizou a Terceira Forma, onde ele se move rapidamente balançando a sua espada de maneira a imitar o movimento das ondas do oceano.",
                Forma="Terceira Forma",
                Dano="3.7k",
                Fôlego="1.8k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/terceira-forma-respiracao.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Uchishio')
    async def Uchishio(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Uchishio",
                Geral="A Quarta Forma da Respiração da Água consiste em uma sequência de golpes consecutivos movendo o corpo de forma fluida semelhante a uma maré.",
                Forma="Quarta Forma",
                Dano="5.1k",
                Fôlego="3.2k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/mere.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Kanten-no-jiu')
    async def Kanten_no_jiu(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Kanten no jiu",
                Geral="Sendo utilizado como golpe final no demônio aranha que representava a “mãe” de Rui, a Quinta Forma é um golpe rápido e sutil que tem como objetivo matar o alvo com pouca ou nenhuma dor.",
                Forma="Quinta Forma",
                Dano="**9.5k** De Dano -> **Em área**",
                Fôlego="5.4k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/8Fifth-Form-Blessed-Rain-910x455.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Nejire-uzu')
    async def Nejire_uzu(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Nejire uzu",
                Geral="Como o próprio nome sugere, para realizar a Sexta Forma o espadachim precisa contorcer rapidamente a parte inferior e superior do seu corpo com o objetivo de criar um redemoinho que corta tudo que está próximo.",
                Forma="Sexta Forma",
                Dano="11.2k",
                Fôlego="6.7k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/Sixth-and-Fourth-Form-ComboFlowing-Water-910x455.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Shizuku-wa-Mondzuki')
    async def Shizuku_wa_Mondzuki(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Shizuku wa Mondzuki",
                Geral="Voltando para a luta Yahaba e Susamaru, a Sétima Forma é um ataque rápido e preciso realizando através de um estocada com a espada. Essa também a mais rápida Forma da Respiração da Água.",
                Forma="Sétima Forma",
                Dano="13.1k",
                Fôlego="7.1k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/Seventh-Form-Drop-Ripple--910x455.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Takitsubo')
    async def Takitsubo(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Takitsubo",
                Geral="Tendo a potência de uma cachoeira, a Oitava Forma seria o equivalente a Primeira Forma, só que realizada com um potente corte vertical em um único golpe.",
                Forma="Oitava Forma",
                Dano="15k",
                Fôlego="8.4k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/Eighth-Form-Waterfall-910x455.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Suiryu-shibuki')
    async def Suiryu_shibuki(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Suiryu shibuki",
                Geral="Simulando a ideia de que o espadachim está pisando brevemente na superfície da água, a Nova Forma é composta por movimentos rápidos e praticamente sem limites, em que o usuário luta sem a necessidade de fixar os pés em uma superfície.",
                Forma="Nona Forma",
                Dano="**18.5k** De Dano -> **Indesviável**",
                Fôlego="10.9k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/Ninth-Form-Splashing-Water-Flow-910x455.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Seisei-ruten')
    async def Seisei_ruten(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Seisei ruten",
                Geral="A última forma utilizada por Tanjiro, a Décima Forma é uma sequência de ataques contínuos que vão ficando cada vez mais fortes à medida que os cortes vão sendo realizados.",
                Forma="Décima Forma",
                Dano="27.8k",
                Fôlego="19.3k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/Kimetsu-no-Yaiba-19-Large-14-910x512.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

    @commands.command(name='Nagi')
    async def Nagi(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=3,
                Nome_Forma="Nagi",
                Geral="Por fim, a Décima Primeira Forma foi criada exclusivamente por Giyu Tomioka, o atual Pilar da Água. Interrompendo todos os movimentos do seu corpo, o espadachim entra em estado de defesa completa desviando e bloqueando qualquer ataque.",
                Forma="Décima Primeira Forma",
                alert="**Desvia/Defende** -> **Menos Os Indesviáveis**",
                Fôlego="20.1k",
                url="https://criticalhits.com.br/wp-content/uploads/2020/03/eleventh-Form-Dead-Calm-910x512.jpg",
                Humano=Humano,
                Oni=False,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Oni:
                    await ctx.reply('__**Você é um Oni. E onis não pode usar respiração :D**__')

                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da água')

def setup(bot):
    bot.add_cog(Água(bot))