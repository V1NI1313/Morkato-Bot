import json
from tokenize import Name
from discord.ext import commands
import discord, random, LPck, asyncio

class Command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Command8')
    async def Command_Add(self, ctx: commands.Context, Made, Name_Command):
        F = LPck.load_json('Json/Server.json')
        Guild = str(ctx.guild.id)

        def check(message):
            return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id 

        print(Name_Command)
        
        if Made.lower() == '--new-command':
            LPck.command_new_message(
                Guild=str(ctx.guild.id),
                Name_Command=str(Name_Command)
            )

        elif Made.lower() == '--add-message':
            try:
                message = await self.bot.wait_for(event='message', timeout=180, check=check)

                LPck.add_messsage(
                    Guild=str(ctx.guild.id),
                    Name_Command=Name_Command.lower(),
                    content=message.content
                )


            except asyncio.TimeoutError:
                await ctx.reply('Você demorou demais, Bye!')

        elif Made.lower() == '--new-embed-command':
            F = LPck.load_json('Json/Server.json')

            Guild = str(ctx.guild.id)

            if not str(Name_Command).lower() in F[Guild]['Commaand']['Embed']:
                    
                F[Guild]['Commaand']['Embed'][str(Name_Command).lower()] = {}
                F[Guild]['Commaand']['Embed'][str(Name_Command).lower()]['title'] = ''
                F[Guild]['Commaand']['Embed'][str(Name_Command).lower()]['description'] = 'None'
                F[Guild]['Commaand']['Embed'][str(Name_Command).lower()]['image'] = None
                F[Guild]['Commaand']['Embed'][str(Name_Command).lower()]['tumb'] = None

                with open('Json/Server.json', 'w') as H:
                    json.dump(F, H, indent=2)

        elif Made.lower() == '--add-description-embed':
            i = 0

            while True:
                await ctx.reply('Qual à descrição do commando?')

                message = await self.bot.wait_for(event='message', timeout=120, check=check)

                Embed = discord.Embed(
                        title=str(F[Guild]['Commaand']['Embed'][str(Name_Command).lower()]['title']),
                        description=message.content,
                        colour=10181046
                    )

                msg = await ctx.send(embed=Embed)

                await msg.add_reaction('✅')
                await msg.add_reaction('❌')

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60, check=lambda r,u: u.id == ctx.author.id)

                if str(reaction.emoji) == '✅':
                    F[Guild]['Commaand']['Embed'][str(Name_Command).lower()]['description'] = message.content

                    with open('Json/Server.json', 'w') as H:
                        json.dump(F, H, indent=2)

                    break

                else:
                    i += 1
                    await msg.delete()

                    if i == 5:
                        await ctx.reply('Foram 5 tentativas e você não gostou de nenhum, complicado')
                        break

def setup(bot):
    bot.add_cog(Command(bot))