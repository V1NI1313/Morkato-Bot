import discord, LPck, RPG
from discord.ext import commands

class Trovão(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.resp = '__**Você não tem à respiração do Trovão**__'
        self.resp_oni = '__**Onis não podem usar respirações**__'
        self.resp_general = '__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__'
        self.verification = [976562964721180682, 988600831978930236]
        self.Humano = [971804637315350558]
        self.Oni = [971804639232143370]
        self.Híbrido = [971804640050040892]

    @commands.command(name='Hekireki-Issen')
    async def Hekireki_Issen(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Hekireki Issen",
                Geral="Zenitsu a usou várias vezes na série, e ao entrar em seu modo inconsciente, é lindo de se testemunhar.",
                Forma="Primeira Forma",
                Dano="**4.5k** De Dano -> **Indesviável**",
                Fôlego="2.3k",
                url="https://c.tenor.com/t9RoDJkcznYAAAAC/kimetsu-no-yaiba-zenitsu.gif",
                Humano=Humano,
                Oni=Oni,
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

    @commands.command(name='Inadama')
    async def Inadama(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Inadama",
                Geral="Zenitsu costumava treinar com uma pessoa, conhecida como Kaigaku, que eventualmente acaba servindo ao Nível Superior Um, Kokushibo. Ele agora é um demônio que pode usar a Respiração do Trovão em um nível absurdo, até mesmos seus raios ficam negros. Essa técnica pode acabar com qualquer caçador de demônio.",
                Forma="Segunda Forma",
                Dano="6.8k",
                Fôlego="4.1k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/respiracao-do-trovao-.jpg",
                Humano=Humano,
                Oni=Oni,
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

    @commands.command(name='Shubun-seirai')
    async def Shubun_seira(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Shubun seirai",
                Geral="Essa técnica pode lançar um raio negro de todas as direções, o que faz dela extremamente poderosa. Quando Kaigaku a usa, ele pode combiná-la com seu raio negro, deixando o alvo ainda mais encrencado.",
                Forma="Terceira Forma",
                Dano="**8k** De Dano -> **Indesviável**",
                Fôlego="5.8k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/forma-.jpg",
                Humano=Humano,
                Oni=Oni,
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

    @commands.command(name='Enrai')
    async def Enrai(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Enrai",
                Geral="Essa técnica envolve uma bola de relâmpago que é fatal para os caçadores de demônios. Contra o alvo, o Trovão Distante pode feri-lo gravemente, se não matar de vez.",
                Forma="Quarta Forma",
                Dano="10k",
                Fôlego="6.3k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/terceira-forma-.jpg",
                Humano=Humano,
                Oni=Oni,
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

    @commands.command(name='Netsu-kairai')
    async def Netsu_kairai(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=3,
                Nome_Forma="Netsu kairai",
                Geral="Quando Kaigaku usa as técnicas do Trovão, todas podem ferir seus oponentes da pior maneira. A quinta forma é altamente veloz, ela permite que o oponente seja atacado mesmo vindo de cima. Embora o oponente seja bastante rápido, ele certamente ainda sofrerá danos.",
                Forma="Quinta Forma",
                alert="**Stun de 2**",
                Fôlego="8k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/forma-cinco-.jpg",
                Humano=Humano,
                Oni=Oni,
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

    @commands.command(name='Dengou-raigou')
    async def Dengou_raigou(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Dengou-raigou",
                Geral="O Rumble Flash é diferente de todas as formas, pois ao ser usada, ele não acaba em um único movimento. Essa técnica lança inúmeros ataques conta o oponente.",
                Forma="Sexta Forma",
                Dano="**15k** De Dano -> **Indefensivel**",
                Fôlego="10.2k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/sexta-forma-.jpg",
                Humano=Humano,
                Oni=Oni,
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

    @commands.command(name='Kami')
    async def Kami(self, ctx: commands.Context, u: str="None"):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Kami",
                Geral="Honoikazuchi No Kami. Ela é semelhante a primeira, mas sua velocidade está em outro patamar.",
                Forma="Sétima Forma",
                Dano="**30k** De Dano -> **Indesviável e Indefensivel**",
                Fôlego="21.7k",
                url="https://nerdhits.com.br/wp-content/uploads/2021/12/setima-forma-.jpg",
                Humano=Humano,
                Oni=Oni,
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
    bot.add_cog(Trovão(bot))