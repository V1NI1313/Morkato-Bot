from random import randint
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions
import discord
import utilsln

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou conectado, como : {self.bot.user}')
        
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="Passos atrás de você"))

        for i in self.bot.guilds:
            for h in i.members:
                print(f'Guilda: {i.name}\nID: {i.id}\n\nMembro: {h.name}\nID {h.id}\n')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not message.author.bot:
            Player = utilsln.Get_User(message.guild, message.author)
            Guild = utilsln.Guild(Guild=message.guild).Command_Info(command=message.content.replace('-', ''))
            

            i = randint(a=0, b=50)
            xp = Player.xp + i
            Sla = Player.set_xp(xp=xp, pop_up=Player.noti)

            if Sla:
                await message.channel.send(f'__**Parabéns {message.author.mention}, Você subiu para o Level `{Player.lv}`**__\n\n\t**╰⌲ ┊ Caso queira tirar essa notificações, de !config-me pop-up `(n/false/não/desativar/d)`**')

            if str(message.content).startswith('-') and Guild.verification:
                channel = self.bot.get_channel(id=message.channel.id)
                Embed = Player.Usar_Command(Name=str(message.content.replace('-', '')))

                if Embed != None:
                    await channel.send(embed=Embed)

                else:
                    await message.reply('__**é necessário eu item para usar esse comando**__')

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, MissingPermissions):
            print('Pwgou')

        else:
            raise error

def setup(bot):
    bot.add_cog(General(bot))

