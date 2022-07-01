from io import BytesIO
import os
from time import sleep
from discord import FFmpegPCMAudio
from discord.ext import commands
import discord, json, asyncio
import  LPck
from pytube import YouTube
from tempfile import TemporaryDirectory

players = {}

class New_item(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Join')
    async def join(self, ctx: commands.Context, mode=1):
        if ctx.author.voice:
            if mode==1:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('https://youtu.be/4IS8ILAq_lU')
                player = voice.play(source)

            else:
                await ctx.reply('Olha deu um erro aqui hein')
                channel = ctx.message.author.voice.channel
                await channel.connect()

        else:
            await ctx.reply('Você não está em nenhum canal de voz!')

        
    @commands.command('Leave')
    async def Leave(self, ctx: commands.Context):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.reply('Tá bom, cês não me querem mais aqui T-T')

        else:
            await ctx.reply('À menos que isso seja uma teoria da conspiração, eu não estou em nenhum canal de voz... Acho que você cê confundiu')

    @commands.command(name='Play')
    async def Play(self, ctx: commands.Context, url):
        """ Kk = []
        for i in os.listdir('songs'):
            if i.endswith('.mp3'):
                Kk.append(f'songs/{i}')"""

        vídeo = YouTube(url=str(url)).streams.get_audio_only()
        voice = ctx.guild.voice_client
        with TemporaryDirectory() as a:
            vídeo.download(a, filename='song.mp3')
            source = FFmpegPCMAudio(f'{a}/song.mp3')
            voice.play(source)
        
 
        """server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)"""
        """player = await voice_client.create_ytdl_player(url)
        players[str(server.id)] = player
        player.start()"""
        print('Aqui')

    @commands.command(name='Stop')
    async def Stop(self, ctx: commands.Context):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()
        

def setup(bot):
    bot.add_cog(New_item(bot))