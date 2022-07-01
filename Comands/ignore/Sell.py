from discord.ext import commands
import discord, random, json, asyncio

from numpy import str0

class Sale(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='pass')
    async def Pass(self, ctx: commands.Context, Member, passar):
        try:
            self.Member = Member.replace('<', '').replace('>', '').replace('@', '')
            self.pp = self.bot.get_user(id=int(self.Member))

            def check(reaction, user):
                if str(reaction.emoji) == '✅' and int(user.id) == int(ctx.author.id):
                    with open('Json/Players.json', 'r') as F:
                        self.F = json.load(F)
                    
                    if self.F[str(ctx.guild.id)][str(ctx.author.id)]['coins'] < int(passar.replace('k', '000')):
                        self.Msg = f"Você Precisária de mais **{int(passar.replace('k', '000')) - self.F[str(ctx.guild.id)][str(ctx.author.id)]['coins']}**R$, Para transfirir para <@{self.Member}>"

                        return str(reaction.emoji) == '✅' and user != self.bot.user

                    elif self.F[str(ctx.guild.id)][str(ctx.author.id)]['coins'] >= int(passar.replace('k', '000')):
                        if int(Member.replace('<', '').replace('>', '').replace('@', '')) != ctx.author.id:
                            self.Msg = f"Você transfiriu **{int(passar.replace('k', '000'))}**R$ Para <@{self.Member}>"
                            self.F[str(ctx.guild.id)][str(self.Member)]['coins'] += int(passar.replace('k', '000'))
                            self.F[str(ctx.guild.id)][str(ctx.author.id)]['coins'] -= int(passar.replace('k', '000'))

                        else:
                            self.Msg = f"**Por que você quer transfirir dinheiro para você mesmo?**"

                        return str(reaction.emoji) == '✅' and user != self.bot.user

            self.msg = await ctx.reply(f"Você está prestes a transfirir para <@{self.Member}> **{int(passar.replace('k', '000'))}**R$. Tem certeza?")
            await self.msg.add_reaction('✅')

            try:
                with open('Json/Players.json', 'r') as F:
                    self.F = json.load(F)

                
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)

                await self.msg.delete()

                with open('Json/Players.json', 'w') as F:
                    self.F = json.dump(self.F, F, indent=4)

                await ctx.reply(self.Msg)

            except asyncio.TimeoutError:
                await self.msg.delete()

        except:
            await ctx.reply('**Assim, eu não sei mais... Eu acho que esse cara não existe!**')

def setup(bot):
    bot.add_cog(Sale(bot))