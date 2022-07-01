import asyncio
import json
import discord, LPck
from discord.ext import commands
import RPG

class Sol(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.verification = [973726923102502912]
        self.Humano = [971804637315350558]
        self.Oni = [971804639232143370]
        self.Híbrido = [971804640050040892]

    @commands.command(name='Enbu-Issen')
    async def Enbu_Issen(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Enbu Issen",
                Geral="Um Corte Vertical Meio Diagonal. Ele Exige Grande Velocidade Nas Pernas, Como Se Estivesse Usando a Técnica Samurai Do Battoujutsu.",
                Forma="Primeira Forma",
                Dano="3.1k",
                Fôlego="1k",
                url="https://c.tenor.com/AlygbzZXIn8AAAAC/tanjiro-demon.gif",
                Humano=Humano, # -> Retorno Verdadeiro ou Falso
                Oni=False, # -> Retorno Verdadeiro ou Falso
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Heki-ra')
    async def Heki_ra(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Heki-ra no Ten",
                Geral="O golpe na segunda forma consiste num anel de fogo que se forma ao redor do usuário por causa da movimentação da lâmina. É muito parecido com a segunda forma da respiração da água.",
                Forma="Segunda Forma",
                Dano="4.2k",
                Fôlego="1.7k",
                url="https://c.tenor.com/t99Es4AlS8IAAAAC/tanjiro-primeiro-sol.gif",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Retsujitsu-Kokyo')
    async def Retsujitsu_Kokyo(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Retsujitsu Kokyo",
                Geral="O usuário movimenta rapidamente a espada na horizontal duas vezes. É ótimo tanto para o ataque, quanto para a defesa.",
                Forma="Terceira Forma",
                Dano="4.6k",
                Fôlego="2.5k",
                url="https://i.im.ge/2022/06/17/rBoCd1.jpg",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Gen-nichi')
    async def Gen_nichin(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                    Modo=3,
                    Nome_Forma="Gen'nichi Ko",
                    Geral="É uma técnica defensiva. Com vários giros, o usuário ganha velocidade para escapar de um lugar rapidamente e ainda deixa para trás a própria imagem, mas feita de chamas.",
                    Forma="Quarta Forma",
                    alert="**Desvia de qualquer ataque** -> **Não sendo indesviável**",
                    Fôlego="3.4k",
                    url="https://i.im.ge/2022/06/17/rBryJK.png",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Kasha')
    async def Kasha(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=2,
                Nome_Forma="Kasha",
                Geral="Esse golpe é como a segunda forma, o anel, todavia, que é formado em chamas ao invés de ser horizontal é vertical. Por isso, essa técnica pode ser usada tanto como uma acrobacia de esquiva, quanto um ataque pelas costas.",
                Forma="Quinta Forma",
                Dano="**Corta o Braço do Adversário.**",
                alert="**É Um Contra Ataque.**",
                Fôlego="4.1k",
                url="https://i.im.ge/2022/06/17/rBrw8S.png",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Shakkotsu')
    async def Shakkotsun(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=3,
                Nome_Forma="Shakkotsu En'yo",
                Geral="Talvez essa seja a técnica defensiva mais forte. Com movimentos circulares, o usuário da técnica consegue defender todos os golpes direto.",
                Forma="Sexta Forma",
                alert="**É Uma Defesa**",
                Fôlego="5.1k",
                url="https://c.tenor.com/Pp6h2dSGlXIAAAAC/hinokami-kagura.gif",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Yokatotsu')
    async def Yokatotsu(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Yokatotsu",
                Geral="Diferente das outras técnicas, essa forma usa a ponta da espada como uma estocada poderosa.",
                Forma="Sétima Forma",
                Dano="7.1k",
                Fôlego="5.6k",
                url="https://popularanime.com.br/wp-content/uploads/2021/12/Tanjiro-using-Sun-Breathing-in-Demon-Slayer-Cropped.jpg",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Hirin-Kagero')
    async def Hirin_Kagero(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Hirin Kagero",
                Geral="Essa forma é puramente ofensiva. Um golpe poderoso é desferido contra o oponente. A diferença é que a lâmina está coberta por chamas e o alcance do golpe fica confuso. Os oponentes acreditam que não foram acertados, mas, na verdade, foram.",
                Forma="Oitava Forma",
                Dano="9.4k",
                Fôlego="7.1k",
                url="https://i.im.ge/2022/06/17/rBuRWJ.png",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Tenshin')
    async def Tenshin(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Tenshin",
                Geral="Essa é uma técnica usada para arrancar a cabeça dos demônios. Isso porque o usuário dá um salto e depois faz um movimento limpo na horizontal. É um golpe poderoso e preciso.",
                Forma="Nona Forma",
                Dano="18.5k",
                Fôlego="9.6k",
                url="https://media.discordapp.net/attachments/954916093863002132/963655342397464596/786200476428402709.png",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Onko')
    async def Onko(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Kiki Onko",
                Geral="Com movimentos em espiral o usuário ganha força e depois a converte num único e poderoso ataque.",
                Forma="Décima Forma",
                Dano="**22.7k** De Dano -> **Indesviável, Só pode ser usado 2x**",
                Fôlego="11.2k",
                url="https://i.im.ge/2022/06/18/rBOQra.png",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Nichiun-no-Ryu')
    async def Nichiun_no_Ryū(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Nichiun no Ryū Kaburimai",
                Geral="Essa é uma das mais poderosas. O usuário desvia dos ataques inimigos enquanto forma um dragão de chamas. Depois ele desfere múltiplos ataques com a espada.",
                Forma="Décima Primeira Forma",
                Dano="**25k** De Dano -> **Em área Indesviável, só poder ser usado 2x**",
                Fôlego="13.5k",
                url="https://i.im.ge/2022/06/18/rBOc8J.png",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Homura-Mai')
    async def Homura_Mai(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Homura Mai",
                Geral="É a mesma da primeira forma, mas agora com dois ataques. Um vertical e outro horizontal.",
                Forma="Décima Segunda Forma",
                Dano="27.6k",
                Fôlego="15k",
                url="https://c.tenor.com/GS9E8UDNdnAAAAAC/sun-breathing-tanjiro.gif",
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
            await ctx.reply('Não tem à respiração do sol')

    @commands.command(name='Fenix')
    async def Fênix(self, ctx: commands.Context, u: str='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=5,
                Nome_Forma="Fênix",
                Geral="É a combinação de todas as formas. Um ataque devastador, muito rápido e completamente OP.",
                Forma="Décima Terceira Forma",
                Dano="•「❤️」**75k** De Dano -> **Só pode ser usado 1x**\n•「❤️」**Hit-Kill** Se For Tsugikuni -> **Só pode ser usado 1x**\n•「💨」**81.1k** De Fôlego\n•「⚠️」**Só Kamado e Tsugikuni podem usar essa forma**",
                Fôlego="20k",
                url="https://1.bp.blogspot.com/-zh2Q4ClGgi8/XsAOPx47pII/AAAAAAAA0M0/XSBspBS99wALSFaFSA9FqpoxMLVzGu8sACK4BGAsYHg/Todas%2Bas%2BFormas%2Bda%2BDan%25C3%25A7a%2Bdo%2BDeus%2Bdo%2BFogo.png",
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
            await ctx.reply('Não tem à respiração do sol')

def setup(bot):
    bot.add_cog(Sol(bot))