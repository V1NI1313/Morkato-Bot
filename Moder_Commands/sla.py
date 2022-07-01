from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '196',
        }],
        'outtmpl': 'song.%(ext)s',
    }

class Sla(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='joinn')
    async def join(self, ctx: commands.Context):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()

        except:
            await ctx.reply('Você precisa estar em um canal de voz!')

    @commands.command(name='leavee')
    async def leavee(self, ctx: commands.Context):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.reply('Tá bom, cês não me querem mais aqui T-T')

        else:
            await ctx.reply('À menos que isso seja uma teoria da conspiração, eu não estou em nenhum canal de voz... Acho que você cê confundiu')

    @commands.command(name='playy')
    async def playy(self, ctx: commands.Context, url=None):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(str(url), download=False)
            URL = info['formats'][0]['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
        else:
            await ctx.send("Já há um som tocando!")
            return
        

def setup(bot):
    bot.add_cog(Sla(bot))