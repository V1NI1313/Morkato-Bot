from io import BytesIO
from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandInvokeError
import  LPck
from PIL import Image, ImageFont, ImageDraw, ImageChops
import utilsln

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

class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['s', 'status'])
    async def Me2(self, ctx: commands.Context, member: commands.Greedy[discord.Member]=[], config: str='None', set: str='None'):
        if member == []:
            Member = utilsln.Get_User(Guild=ctx.guild, User=ctx.author)

        elif not member == []:
            Member = utilsln.Get_User(Guild=ctx.guild, User=member[0])

        if config.lower() == '--set-xp':
            Member.set_xp(xp=int(set))
        
        if True:
            Main_Image = Image.open('Img/base.png').convert('RGBA')
            Img_gg = Image.open(str(Member.banner)).convert('RGBA')

            img_url = Member.url
            data = BytesIO(await img_url.read())
            img_url = Image.open(data).convert('RGBA')
            avatar = circle(img_url, size=(215, 215))

            Font_Index = ImageFont.truetype('Img/open-sans.light.ttf', 38)
            Image_edit = ImageDraw.Draw(Main_Image)

            text = str(Member.name)

            xp = str(Member.xp)
            level = str(Member.lv)
            level_final = str(Member.lvrun)
            money = str(LPck.num_fmt(int(Member.money)))
        
            Image_edit.text((280,240), text, (255,255,255), font=Font_Index)
            Image_edit.text((65,490), xp, (255,255,255), font=Font_Index)
            Image_edit.text((405,490), level, (255,255,255), font=Font_Index)
            Image_edit.text((405,635), level_final, (255,255,255), font=Font_Index)
            Image_edit.text((65,635), money, (255,255,255), font=Font_Index)


            Main_Image.paste(avatar, (56,158), avatar)

            Img_gg.paste(Main_Image, (0,0), Main_Image)

            with BytesIO() as a:
                Img_gg.save(a, 'png')
                a.seek(0)
                await ctx.send(file=discord.File(a, 'card.png'))


def setup(bot):
    bot.add_cog(Status(bot))