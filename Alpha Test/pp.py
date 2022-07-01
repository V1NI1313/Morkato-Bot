import asyncio
from discord.ext import commands
import discord
import utilsln
import json

class Pp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def Usar(self, ctx: commands.Context, Name, Q: int=1):
        Player = utilsln.Get_User(Guild=ctx.guild, User=ctx.author)
        Item = utilsln.Guild(ctx.guild).Item_Info(Name=Name)

        Verification = Player.Usar(Name=Name, Q=Q)

        if Verification:
            await ctx.send(embed=Item.Embed)

        elif not Verification:
            await ctx.reply('Não tem')

    @commands.command(aliases=['New-Command'])
    async def New_Command(self, ctx: commands.Context, Name):
        Guild = utilsln.Guild(Guild=ctx.guild)

        Command = Guild.New_Command(Name=str(Name))

        if Command:
            await ctx.reply(f'__**Um comando chamado `{Name}` Foi criado**__')

    @commands.command(aliases=['Get-Item'])
    async def Get_Item(self, ctx: commands.Context, Name, Q: int=1):
        Player = utilsln.Get_User(Guild=ctx.guild, User=ctx.author)
        Guild = utilsln.Guild(Guild=ctx.guild)

        Item = Player.Get_Item(Name=Name, Q=Q)

        if Item:
            await ctx.reply(f'__**O Item chamado `{Name}` foi colocado no inv de {ctx.author.mention}, Quantidade: `{Q}`, Ele tem `{Player.inv[str(Name)] + Q}`**__')

        elif not Item:
            await ctx.reply('__**Esse Item não existe**__')

    @commands.command(aliases=['Vincular-Item'])
    async def Vincular_Item(self, ctx: commands.Context, item, command, Q: int=1):
        Guild = utilsln.Guild(Guild=ctx.guild)

        Item = Guild.Item_Info(Name=item)
        Command = Guild.Command_Info(command=command)

        Verification = Guild.Vincular_Item(command=command, item=item, Q=Q)

        if Verification:
            await ctx.reply(f'__**O Item chamado `{item}` foi vinculado ao comando `{command}`, Quantidade: `{Q}`**__')

        elif not Verification:
            if not Item.verification and Command.verification:
                await ctx.reply('__**Esse Item não existe**__')

            elif not Command.verification and Item.verification:
                await ctx.reply('__**Esse Comando não existe**__')

            else:
                await ctx.reply('__**Esse Item e Comando não existe**__')

    @commands.command()
    async def Usar_i(self, ctx, name):
        Player = utilsln.Get_User(Guild=ctx.guild, User=ctx.author)
        Guild = utilsln.Guild(Guild=ctx.guild)

        Embed = Player.Usar_Command(Name=name)

        if not Embed == None and not Embed == 0:
            await ctx.send(embed=Embed)

        elif Embed == 0:
            await ctx.send('__**Esse comando não existe**__')

        else:
            await ctx.send('__**É necessário um Item para usar esse comando**__')

    @commands.command(aliases=['edit-command'])
    async def Commandd(self, ctx: commands.Context, Type, Name):
        Guild = utilsln.Guild(Guild=ctx.guild)
        Command = Guild.Command_Info(command=Name)

        if Command.verification:
            try:
                if str(Type).lower() == '--set-title':
                    await ctx.reply('Titulo?')
                    message_title = await self.bot.wait_for('message', timeout=30, check=lambda message: message.author.id == ctx.author.id)

                    Command.edit(title=message_title.content, description=None, tumb=None, url=None)
                
                if str(Type).lower() == '--set-description':
                    await ctx.reply('descrição?')
                    message_description = await self.bot.wait_for('message', timeout=30, check=lambda message: message.author.id == ctx.author.id)

                    Command.edit(title=None, description=message_description.content, tumb=None, url=None)

                if str(Type) == '--set-url':
                    await ctx.reply('url?')
                    message_url = await self.bot.wait_for('message', timeout=30, check=lambda message: message.author.id == ctx.author.id)

                    Command.edit(title=None, description=None, tumb=None, url=message_url.content)

            except asyncio.TimeoutError:
                await ctx.replu('Você demorou muito, Bye')

            except:
                raise

    @commands.command(aliases=['edit-item'])
    async def itemm(self, ctx: commands.Context, Type, Name):
        Guild = utilsln.Guild(Guild=ctx.guild)
        Item = Guild.Item_Info(Name=Name)

        if Item.verification:
            try:
                if str(Type).lower() == '--set-title':
                    await ctx.reply('Titulo?')
                    message_title = await self.bot.wait_for('message', timeout=30, check=lambda message: message.author.id == ctx.author.id)

                    Item.edit(title=message_title.content, description=None, tumb=None, url=None)
                
                if str(Type).lower() == '--set-description':
                    await ctx.reply('descrição?')
                    message_description = await self.bot.wait_for('message', timeout=30, check=lambda message: message.author.id == ctx.author.id)

                    Item.edit(title=None, description=message_description.content, tumb=None, url=None)

                if str(Type) == '--set-url':
                    await ctx.reply('url?')
                    message_url = await self.bot.wait_for('message', timeout=30, check=lambda message: message.author.id == ctx.author.id)

                    Item.edit(title=None, description=None, tumb=None, url=message_url.content)

            except asyncio.TimeoutError:
                await ctx.replu('Você demorou muito, Bye')

            except:
                raise

    @commands.command(name='Command-Info')
    async def Command_Info(self, ctx: commands.Context, *, Name: str):
        Guild = utilsln.Guild(Guild=ctx.guild)
        Command = Guild.Command_Info(command=Name)

        if Command.verification:
            await ctx.send(embed=Command.Embed_Info)

        elif not Command.verification:
            await ctx.reply('__**Esse comando não existe**__')

    @commands.command('config-me')
    async def Me(self, ctx, args, a):
        if str(args) == 'pop-up':
            if str(a) in ['n', 'false', 'falso', "desativar", 'd']:
                with open('Json/P.json', 'r', encoding='utf-8') as F:
                    F = json.load(F)

                F[str(ctx.guild.id)][str(ctx.author.id)]['config']['noti'] = False

                with open('Json/P.json', 'w') as H:
                    json.dump(F, H, indent=2)

def setup(bot):
    bot.add_cog(Pp(bot))