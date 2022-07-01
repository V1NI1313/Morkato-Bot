from discord.ext import commands
import RPG

class Lua(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.verification = [974791180472709121]
        self.Humano = [971804637315350558]
        self.Oni = [971804639232143370]
        self.Híbrido = [971804640050040892]

    @commands.command(name='Yoi-no-Miya')
    async def Yoi_no_Miya(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Yoi no Miya",
                Geral="Kokushibo saca sua espada e faz um corte amplo em um único movimento, fazendo com que várias luas crescentes surjam no local do corte, algo que se repete em todas as formas desta respiração.",
                Forma="Primeira Forma",
                Dano="**Corta a mão do adversário**",
                Fôlego="3.1k",
                url="https://1.bp.blogspot.com/-vxku7PeRBX0/XlfTtJypC0I/AAAAAAAAzVs/zHVf1AwhNpghM0Uo-Ipa39unT_kwxtxBwCLcBGAsYHQ/s1600/Todas%2Bas%2BFormas%2Bda%2BRespira%25C3%25A7%25C3%25A3o%2Bda%2BLua%2BPrimeira%2BForma.png",
                Humano=Humano,
                Oni=Oni,
                Híbrido=Hibrido
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Rogetsu')
    async def Rogetsu(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Rogetsu",
                Geral="Kokushibo faz vários cortes no ar que o defendem de ataques próximos enquanto criam uma barragem de luas crescentes.",
                Forma="Segunda Forma",
                Dano="3.1k",
                Fôlego="1.8k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/segunda-forma-respiracao-da-lua-910x664.jpg",
                Humano=Humano,
                Oni=Oni,
                Híbrido=Hibrido
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Tsugari')
    async def Tsugari(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Tsugari",
                Geral="Kokushibo cria uma verdadeira tempestade de pequenas luas crescentes, causando uma grande destruição em área.",
                Forma="Terceira Forma",
                Dano="3.7k",
                Fôlego="2k",
                url="https://1.bp.blogspot.com/-QAa933dalyE/XlfX-5vyjQI/AAAAAAAAzWM/yz8dN0-MVg4M47m8xCZqpu7zclcQiCVvQCLcBGAsYHQ/s1600/Todas%2Bas%2BFormas%2Bda%2BRespira%25C3%25A7%25C3%25A3o%2Bda%2BLua%2BTerceira%2BForma.png",
                Humano=Humano,
                Oni=Oni,
                Híbrido=Hibrido
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Geppaku-Saika')
    async def Geppaku_Saika(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Geppaku Saika",
                Geral="Kokushibo faz vários cortes curvados um em cima do outro, criando uma espécie de vórtex. Sanemi comentou que o vilão fez este ataque sem balançar sua lâmina uma única vez, o que é pra lá de impressionante.",
                Forma="Quinta Forma",
                Dano="5.1k",
                Fôlego="3.1k",
                url="https://c.tenor.com/hkgYjang5HUAAAAM/discord-rp-respira%C3%A7%C3%A3o-da-lua.gif",
                Humano=Humano,
                Oni=Oni,
                Híbrido=Hibrido
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Muken')
    async def Muken(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Muken",
                Geral="Esta técnica foi forte o suficiente para cortar múltiplos Hashiras e sobrepujar Sanemi Shinazugawa, o Hashira do Vento.",
                Forma="Sexta Forma",
                Dano="8.1k",
                Fôlego="5.2k",
                url="https://1.bp.blogspot.com/-at2QhxhvQsY/XlfWzAMYumI/AAAAAAAAzWA/LZ2gxPJ1c58R8zEfwALTqxBYsQc3YPV2QCLcBGAsYHQ/s1600/Todas%2Bas%2BFormas%2Bda%2BRespira%25C3%25A7%25C3%25A3o%2Bda%2BLua%2BSexta%2BForma.png",
                Humano=Humano,
                Oni=Oni,
                Híbrido=Hibrido
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Zukibae')
    async def Zukibae(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Zukibae",
                Geral="Kokushibo cria uma verdadeira onda de destruição em várias direções, forte o suficiente para deixar marcas profundas no chão, e empurrar dois Hashiras para trás com facilidade.",
                Forma="Sétima Forma",
                Dano="**11.1k** De Dano -> **Indesviável**",
                Fôlego="5.3k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/setima-forma-respiracao-da-lua-910x1067.jpg",
                Humano=False,
                Oni=Oni,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Humano:
                    await ctx.reply('__**Somente da sexta forma para baaixo que os Humanos podem usar :D**__')
                
                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Geppaku-Saika')
    async def Geppaku_Saika(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Geppaku Saika",
                Geral="Kokushibo triplica o alcance de seu ataque e cria um corte gigantesco que diminui de tamanho lentamente, enquanto incontáveis luas crescentes afiadas surgem no local do ataque.",
                Forma="Oitava Forma",
                Dano="12.6k",
                Fôlego="6.3k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/oitava-forma-respiracao-da-lua-910x1401.jpg",
                Humano=False,
                Oni=Oni,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Humano:
                    await ctx.reply('__**Somente da sexta forma para baaixo que os Humanos podem usar :D**__')
                
                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Kudaritsuki')
    async def Kudaritsuki(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Kudaritsuki",
                Geral="A nova forma é capaz de acertar inimigos a uma longa distância, tornando esta uma das formas mais poderosas da Respiração da Lua.",
                Forma="Nona Forma",
                Dano="**13.9k** De Dano -> **Em área**",
                Fôlego="6.9k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/nona-forma-respiracao-da-lua-910x1413.jpg",
                Humano=False,
                Oni=Oni,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Humano:
                    await ctx.reply('__**Somente da sexta forma para baaixo que os Humanos podem usar :D**__')
                
                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Senmenzan')
    async def Senmenzan(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=1,
                Nome_Forma="Senmenzan",
                Geral="Com a décima forma, Kokushibo cria um enorme corte em três camadas que é capaz de partir qualquer um que seja atingido em três partes.",
                Forma="Décima Forma",
                Dano="16.7k",
                Fôlego="9.6k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/decima-forma-respiracao-da-lua-910x1421.jpg",
                Humano=False,
                Oni=Oni,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Humano:
                    await ctx.reply('__**Somente da sexta forma para baaixo que os Humanos podem usar :D**__')
                
                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Kyohen')
    async def Kyohen(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Kyohen",
                Geral="Kokushibo balança sua espada e cria um vórtex extremamente caótico de cortes multidirecionais capazes de destruir qualquer coisa que esteja em seu alcance.",
                Forma="Décima Quarta Forma",
                Dano="21.1k De Dano -> **Indesviável, em área**",
                Fôlego="13.5k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/decima-quarta-forma-respiracao-da-lua-910x956.jpg",
                Humano=False,
                Oni=Oni,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Humano:
                    await ctx.reply('__**Somente da sexta forma para baaixo que os Humanos podem usar :D**__')
                
                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')

    @commands.command(name='Gekko')
    async def Gekko(self, ctx: commands.Context, u='None'):
        Verification = RPG.Roles_Verification(User=ctx.author, Role=self.verification, u=u)
        Humano = RPG.Roles_Verification(User=ctx.author, Role=self.Humano, u='None')
        Oni = RPG.Roles_Verification(User=ctx.author, Role=self.Oni, u='None')
        Hibrido = RPG.Roles_Verification(User=ctx.author, Role=self.Híbrido, u='None')

        Embed = RPG.Message_Respiração(
                Modo=4,
                Nome_Forma="Gekko",
                Geral="Esta é a forma mais poderosa da Respiração da Lua que conhecemos. Com ela, Kokushibo cria uma multitude de cortes crescentes mirados no chão, resultando em seis golpes ao mesmo tempo que caem na direção de seus oponentes.",
                Forma="Décima Sexta Forma",
                Dano="**28.5k** De Dano -> **Indesviável**",
                Fôlego="15.8k",
                url="https://criticalhits.com.br/wp-content/uploads/2021/01/decima-sexta-forma-respiracao-da-lua-910x1033.jpg",
                Humano=False,
                Oni=Oni,
                Híbrido=Hibrido,
                user=Verification,
                npc=u
            )

        if Verification:
            try:
                await ctx.send(embed=Embed)

            except:
                if Humano:
                    await ctx.reply('__**Somente da sexta forma para baaixo que os Humanos podem usar :D**__')
                
                else:
                    await ctx.reply('__**Você não é Humano Nem Oni. Como que você quer usar essa respiração?**__')

        elif not Verification:
            await ctx.reply('Não tem à respiração da Lua')



def setup(bot):
    bot.add_cog(Lua(bot))