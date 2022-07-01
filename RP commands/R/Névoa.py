import asyncio
import json
from discord.ext import commands
import RPG

class Névoa(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.resp = '__**Você não tem à respiração da névoa**__'
        self.resp_oni = '__**Onis não podem usar respirações**__'
        self.resp_general = '__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__'
        self.verification = [976596561305935902]
        self.Humano = [971804637315350558]
        self.Oni = [971804639232143370]
        self.Híbrido = [971804640050040892]

    @commands.command(name='Suiten-Togasumi')
    async def Suiten_Togasumi(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Suiten Tōgasumi",
                Geral="O espadachim usa um ataque perfurador no adversário em frente a ele.",
                Forma="Primeira Forma",
                Dano="3.4k",
                Fôlego="1.8k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-01.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)

    @commands.command(name='Yaekasumi')
    async def Yaekasumi(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Yaekasumi",
                Geral="O usuário da Respiração da Névoa usa oito cortes de espada, um em cima do outro, em rápida sucessão.",
                Forma="Segunda Forma",
                Dano="4.5k",
                Fôlego="3.1k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-02.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)

    @commands.command(name='Kasan-Shibuki')
    async def Kasan_no_Shibuki(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=3,
                Nome_Forma="Kasan no Shibuki",
                Geral="O espadachim usa um corte circular que repele ataques de projéteis.",
                Forma="Terceira Forma",
                alert="É uma defesa",
                Fôlego="3.5k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-03.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)

    @commands.command(name='Iryugiri')
    async def Iryugiri(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Iryūgiri",
                Geral="O usuário retira rapidamente a espada da bainha e acerta o adversário, numa técnica semelhante ao estilo Iaido.",
                Forma="Quarta Forma",
                Dano="6.1k",
                Fôlego="4.2k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-04.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)
        
    @commands.command(name='Kaun-Umi')
    async def Kaun_no_Umi(self, ctx: commands.Context, u: str=None):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Kaun no Umi",
                Geral="O usuário avança em direção ao inimigo em alta velocidade e dispara uma série de ataques que cobrem uma grande área.",
                Forma="Quinta Forma",
                Dano="7.5k",
                Fôlego="5.4k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-05.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)

    @commands.command(name='Tsuki-Kasho')
    async def Tsuki_no_Kashō(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Tsuki no Kashō",
                Geral="O usuário da Respiração da Névoa pula no ar e então dispara uma série de cortes distantes que cobrem uma grande área.",
                Forma="Sexta Forma",
                Dano="15.4k",
                Fôlego="8k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-06-910x640.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)

    @commands.command(name='Oboro')
    async def Oboro(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=5,
                Nome_Forma="Oboro",
                Geral="Criação do próprio Tokito, onde ele muda o ritmo dos movimentos dele para desorientar o inimigo ocultando assim a própria presença. Quando ele se apresenta ao inimigo, a velocidade dele parece extremamente lenta, mas quando ele se esconde, ele se movimenta rapidamente. Esta técnica foi capaz de desorientar o Lua Superior 5, Gyokko e assim derrotá-lo.",
                Forma="Sétima Forma",
                Dano="•「⚠️」**Uma névoa que diminui 2 no roll do adversário**\n•「⚠️」**Aumenta 2 no desvio**\n•「⚠️」**Aumenta em 10k de dano em todas às formas**\n•「💨」**12k** De Fôlego",
                url="https://criticalhits.com.br/wp-content/uploads/2021/05/respiracao-da-nevoa-07.jpg",
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
                    await ctx.reply(self.resp_oni)

                else:
                    await ctx.reply(self.resp_general)

        elif not Verification:
            await ctx.reply(self.resp)

def setup(bot):
    bot.add_cog(Névoa(bot))