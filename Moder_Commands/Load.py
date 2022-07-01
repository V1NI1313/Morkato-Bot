import os, json
from random import randint
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageChops
import discord
from io import BytesIO

def circle(pfp,size = (215,215)):
    
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


class GG(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='banner')
    async def Teste(self, ctx: commands.Context):

        Kk = []

        for i in os.listdir('Img/gg'):
            if i.endswith('.png') and not i == 'base.png' and not i == 'base2.png' and not i == 'card.png':
                Kk.append(i)

        
        Gg = 0
        msg = await ctx.reply(file=discord.File(f'Img/gg/{Kk[Gg]}', 'Background.png'))

        await msg.add_reaction('◀')
        await msg.add_reaction('✅')
        await msg.add_reaction('▶')

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if str(reaction) == '◀':
                if i > 0:
                    i -= 1
                    await msg.delete()
                    msg = await ctx.reply(file=discord.File(f'Img/gg/{Kk[i]}', 'Background.png'))

                    await msg.add_reaction('◀')
                    await msg.add_reaction('✅')
                    await msg.add_reaction('▶')

            elif str(reaction) == '▶':
                if i < 2:
                    i += 1
                    await msg.delete()
                    msg = await ctx.reply(file=discord.File(f'Img/gg/{Kk[i]}', 'Background.png'))

                    await msg.add_reaction('◀')
                    await msg.add_reaction('✅')
                    await msg.add_reaction('▶')

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = check)

                if str(reaction.emoji) == '✅':
                    self.Main_Image = Image.open('Img/base.png').convert('RGBA')
                    self.Img_gg = Image.open(f'Img/{Kk[i]}')

                    self.img_url = ctx.author.avatar_url_as(size=256)
                    data = BytesIO(await self.img_url.read())
                    self.img_url = Image.open(data).convert('RGBA')
                    self.avatar = circle(self.img_url, size=(215, 215))

                    self.Main_Image.paste(self.avatar, (56,158), self.avatar)

                    self.Img_gg.paste(self.Main_Image, (0,0), self.Main_Image)

                    with BytesIO() as a:
                        self.Img_gg.save(a, 'png')
                        a.seek(0)
                        msg = await ctx.send(file=discord.File(a, 'card.png'))

                        await msg.add_reaction('✅')
                        await msg.add_reaction('❌')

                        reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = check)

                        if str(reaction.emoji) == '✅':
                            with open('Json/Players.json', 'r', encoding='utf-8') as F:
                                F = json.load(F)

                            F[str(ctx.guild.id)][str(ctx.author.id)]['config']['baner'] = str(f'Img/{Kk[i]}')

                            with open('Json/Players.json', 'w') as H:
                                json.dump(F, H, indent=2)

                            break

                        elif str(reaction.emoji) == '❌':
                            await ctx.reply('Que pena que você não gostou T-T')
                            break

            except:
                break

        await msg.clear_reactions()

    @commands.command(name='ban')
    async def _(self, ctx: commands.Context, user: discord.Member, *, reason: str=None):
        await user.ban(reason=reason)

    @commands.command(aliases=['make_role', 'bah'])
    @commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
    async def create_role(self, ctx, *, name):
        KGO = str(name).split(',')
        Kk = []
        guild = ctx.guild
        f = 0
        color = [0x9B59B6, 0xF1C40F, 0x992D22, 0xFFFF00, 0x1ABC9C, 0x3498DB]

        
        for i in KGO:
            if not i[f] == ' ':
                Kk.append(i)
            else:
                f += 1
        
        for i in Kk:
            random = randint(0, len(color)-1)
            GG = str(i).replace('\n', '')
            role = await guild.create_role(name=GG)
            await role.edit(color=color[random])

            await ctx.send(f'O cargo chamado: `{str(GG)}` foi criado')

    @commands.command(aliases=['delete_role', 'bahh'])
    @commands.has_permissions(manage_roles=True)
    async def delrole(self, ctx, role: commands.Greedy[discord.Role], *, content: str='Olá'):
        Kk = []
        if role[0]:
            try:
                for i in role:
                    await i.delete()
                    Kk.append("O cargo: `{0}` Foi deletado. Motivo: **{1}**!".format(i.name, content))

                await ctx.reply('\n'.join(Kk))
            except discord.Forbidden:
                await ctx.send('Eu preciso da permissão "Gerenciar cargos" Para que eu possa apagar esse cargo :D')
        else:
            await ctx.send("Esse cargo não existe!")

    @commands.command(aliases=['member-info'])
    async def ______________(self, ctx, member: str=None, *, content: str='GGGGGGGGGGGG POHA'):
        kk = await commands.MemberConverter().convert(ctx=ctx, argument=member)
        print(kk)

    @commands.command(name='sla')
    async def ___(self, ctx: commands.Context, role: discord.Role, *, name: str=''):
        
        position = int(role.position)
        guild = ctx.guild

        role = await guild.create_role(name=name)
        await role.edit(position=position)

    @commands.command(name='hhh')
    async def ____(self, ctx: commands.Context, *, name: discord.Role):
        print(name.position)

def setup(bot):
    bot.add_cog(GG(bot))