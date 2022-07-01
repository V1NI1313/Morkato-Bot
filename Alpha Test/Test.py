import os
from time import sleep
from click import edit
from discord.ext import commands
import discord, json, asyncio
import  LPck
import utilsln
import tempfile

class Alpha(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
        self.Kk = {'Channels': ['🍮 - Pudim -🍮', '🍮 Pudim🍮', 'geral', 'sla', 'gg', 'vai', 'tomar', 'no', 'dd', 'a']}

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Testr(self, ctx: commands.Context, member: commands.Greedy[discord.Member]=None):
        guild = ctx.guild

        if member == None:
            for i in guild.members:
                user = LPck.load_json('Json/Players.json')
                
                if str(i.id) in user[str(guild.id)]:
                    if user[str(guild.id)][str(i.id)]['status']['xp'] <= 10:
                        del user[str(guild.id)][str(i.id)]

                        with open('Json/Players.json', 'w') as H:
                            json.dump(user, H, indent=2)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def url(self, ctx: commands.Context, Parametro: str='', *, test: int=1):
        Guild = ctx.guild
        Member = ctx.author

        Player = utilsln.Get_User(Guild=Guild, User=Member)

        if Parametro.lower() == '--test':
            Player.set_xp(xp=test)

            await ctx.reply(f"Xp: {str(Player.xp)}" + '\n' + f'Level: {str(Player.lv)}')

        elif Parametro.lower() == '--status':
            await ctx.reply(f'Xp: {Player.xp}\nLevel: {Player.lv}')

        elif Parametro.lower() in ['--set-lv', '--set-level']:
            Player.set_lv(Level=test)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def l(self, ctx: commands.Context, Parametro: str='', *, channels: str):
        chanels = str(channels).split(',')
        guild = ctx.guild

        sla = await guild.create_category(name=Parametro)

        for i in chanels:
            await sla.create_text_channel(name=i)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Mgh(self, ctx):
        Guild = utilsln.Guild(Guild=ctx.guild)

        await ctx.reply(f'{Guild.name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Item_info(self, ctx: commands.Context, *, parametro: str):
        Guild = utilsln.Guild(Guild=ctx.guild)
        Item = Guild.Item_Info(str(parametro))
        sla = ', '.join(Item.command_vin)

        if Item.verification:
            Embed = discord.Embed(
                title=f'O titulo do seu Item é:\n**```{Item.title}```**',
                description=f'A descrição do seu Item é:\n\n**```{Item.description}```**\n\nA imagem do seu item é:\n\n**```{Item.url}```**\n\n A tumb do seu item é:\n\n**```{Item.tumb}```**\nComando(dos) Vinculado(dos) do seu item é:\n\n**```{sla}```**\n\nSeu item na loja é:\n\n**```{Item.custo}```**',
                colour=0x9B59B6
            )

            if Item.url != None:
                Embed.set_image(url=Item.url)

            if Item.tumb != None:
                Embed.set_thumbnail(url=Item.tumb)

            await ctx.reply(embed=Embed)

        if not Item.verification:
            await ctx.reply('__**Esse item não existe!**__')

    @commands.command(name='new-item')
    async def new(self, ctx: commands.Context, Name):
        Guild = utilsln.Guild(Guild=ctx.guild)

        Guild.New_Item(Name=Name)

        await ctx.reply(f'__**Um item chamado `{Name}` foi criado**__')

    @commands.command()
    async def pudim(self, ctx: commands.Context):
        with open('Json/config.json', 'r') as Tk:
            Tk = json.load(Tk)

        if not ctx.author.id == 510948690354110464:
            await ctx.reply('Contemplem o 🍮')
        
        else:
            Tk['pô'] = {}
            Tk['pô']['sla'] = []
            uild = ctx.guild.text_channels

            await ctx.reply('🍮 - Para Você, 🍮 - Para todos')

            for i in ctx.guild.members:
                try:
                    await i.edit(nick='🍮 - Pudim -🍮')

                except:
                    pass

    @commands.command()
    async def slap(self, ctx):
        with open('Json/config.json', 'r') as Tk:
            Tk = json.load(Tk)

        Guild = ctx.guild

        for i in Guild.members:
            try:
                await i.edit(nick=i.name)

            except:
                pass

    @commands.command(name='troll')
    async def _________________(self, ctx: commands.Context, c: int):
        channel = ctx.channel
        messages = await channel.history(limit=int(c + 1)).flatten()

        msg = await ctx.send(f'**Esse canal teve {c} mensagens deletadas por {ctx.author.mention}**')

        for i in messages:
            if not i == msg:
                await i.delete()

def setup(bot):
    bot.add_cog(Alpha(bot))