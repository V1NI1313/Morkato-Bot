from discord.ext import commands
import discord, json, asyncio
import  LPck

class Me(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Me')
    async def Me(self, ctx: commands.Context, command: str='None', user: str=None, reset: int=None):
        with open('Json/Players.json', 'r') as F:
            self.F = json.load(F)

        if command.lower() == '--reset-all-users-default':
            if ctx.author.guild_permissions.administrator:
                # LP.create_player_defaukt(Server=str(ctx.guild.id), Player=str(i))

                await ctx.reply('Todos usuários foram resetados com sucesso')

            else:
                await ctx.reply('**Perdão aê, mais você não pode executar esse comando!**')

        elif '--set' in command.lower():
            # self.F[str(ctx.guild.id)][user.replace('<', '').replace('>', '').replace('@', '')]
            if ctx.author.guild_permissions.administrator:
                if user != None:
                    try:
                        self.sla = self.bot.get_user(id=int(user.replace('<', '').replace('>', '').replace('@', '')))

                        if command.lower().replace('--set-', '') == 'xp':
   
                            try:
                                LPck.set_xp(Server=str(ctx.guild.id), Player=str(user.lower().replace('<', '').replace('>', '').replace('@', '')), xp=reset)

                            except:
                                await ctx.reply('Aconteceu alguma coisa... Não estou conseguindo setar')

                        elif command.lower().replace('--set-', '') in ['level', 'lv']:

                            try:
                                LPck.set_lv(Server=str(ctx.guild.id), Player=str(user.lower().replace('<', '').replace('>', '').replace('@', '')), level=reset)

                            except:
                                await ctx.reply('Aconteceu alguma coisa... Não estou conseguindo setar')

                        await ctx.reply(f'**{user}, Foi setado com sucesso!**')

                    except:
                        await ctx.reply('Não sei quem é esse Player')
                
                else:
                    await ctx.reply('**Assim como eu vou saber quem você quer setar... Acho que você esqueceu**')

            else:
                await ctx.reply('**Perdão aê, mais você não pode executar esse comando!**')


        elif command == 'None':    
            self.F = LPck.get_player(Server=str(ctx.guild.id), Player=str(ctx.author.id))
            
            self.url = ctx.author.avatar_url
            
            self.Embed = discord.Embed(
                title=ctx.author.name + '\n_______________',
                description="",
                colour=7419530
            )

            self.Embed.set_thumbnail(url=self.url)

            self.Embed.add_field(name=f'{ctx.author.name} Status:', value=f"**XP**: {self.F['status']['xp']}\n**Nivel**: {self.F['status']['level']}, **Próximo Level com {self.F['status']['level_final']}**\n**Coin:** {self.F['status']['money']}")

            """self.Embed.add_field(name='XP:', value=f'**{self.F[str(ctx.guild.id)][str(ctx.author.id)]["xp"]}** De Xp\n', inline=True)
            self.Embed.add_field(name='Level:', value=f'**{self.F[str(ctx.guild.id)][str(ctx.author.id)]["level"]}** De Level\n', inline=True)
            self.Embed.add_field(name='Próximo Level:', value=f'**{self.F[str(ctx.guild.id)][str(ctx.author.id)]["level_Chegar"]}** De Xp\n', inline=True)
            self.Embed.add_field(name='Coin:', value=f'**{self.F[str(ctx.guild.id)][str(ctx.author.id)]["coins"]}** De Moedas', inline=True)"""

            await ctx.send(embed=self.Embed)

def setup(bot):
    bot.add_cog(Me(bot))