from discord.ext import commands
import discord, json, asyncio
import  LPck

class New_item(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='New-Item')
    async def new_item(self, ctx: commands.Context, Command):
        
        Name = 'Json/Server.json'
        F = LPck.load_json(Name)

        def check_message(message):
            return  message.author.id == ctx.author.id

        if not str(ctx.guild.id) in F:
            LPck.create_json_default(Server=str(ctx.guild.id))

        # --------------------------------------------------------------------------------------
        try:
            await ctx.reply('Titulo?')
            message_Name = await self.bot.wait_for('message', timeout=180, check=check_message)

            await ctx.reply('Qual à descrição?')
            message_description = await self.bot.wait_for('message', timeout=180, check=check_message)

        except asyncio.TimeoutError:
            await ctx.reply('Você demorou demais, bye!')

        await ctx.reply('Quanto de dinheiro esse comando irá tirar?')
        
        while True:
            try:
                message_Sell = await self.bot.wait_for('message', timeout=180, check=check_message)
                Kk = []

                for i in range(len(message_Sell.content)):
                    Kk.append(message_Sell.content[i])

                while Kk[0] == ' ':
                    Kk.pop(0)

                messageSell = ''.join(Kk).lower().replace('k', '000').replace('m', '000000')

                if not messageSell[0] == '0':
                    messageSell = int(messageSell)
                    break

                else:
                    await ctx.reply('K, isso não funciona comigo rs')

            except asyncio.TimeoutError:
                await ctx.reply('Você demorou demais, bye!')
                break

            except:
                await ctx.reply('Ok, mais só pode numeros Blz?')

        await ctx.reply('Qual à Imagem **(Caso não queira digite "no" ou "Não")**?')
        message_url = await self.bot.wait_for('message', timeout=180, check=check_message)

        if message_url.content.lower() == 'no' or message_url.content.lower() == 'não' or message_url.content.lower() == 'done':
            message_url.content = None

        # --------------------------------------------------------------------------------------

        Item = LPck.new_item(
            Server=str(ctx.guild.id),
            Name_Command=str(Command).lower(),
            Name=message_Name.content,
            description=message_description.content,
            Sell=messageSell,
            url=message_url.content
        )

        Embed = discord.Embed(
            title=message_Name.content,
            description=message_description.content,
            colour=7419530
        )

        if not message_url.content == None:
            Embed.set_image(url=message_url.content)

        await ctx.reply(embed=Embed)

    @commands.command(name='Comprar')
    async def Comprar(self, ctx: commands.Context, Command, Quantidade: int=1):
            
            Name = 'Json/Server.json'

            F = LPck.load_json(Name)

            if Command.lower() in F[str(ctx.guild.id)]['Shop']:
                Embed = discord.Embed(
                title=F[str(ctx.guild.id)]['Shop'][str(Command).lower()]['name'],
                description=F[str(ctx.guild.id)]['Shop'][str(Command).lower()]['description'],
                colour=7419530
            )

            if not F[str(ctx.guild.id)]['Shop'][str(Command).lower()]['url'] == None:
                Embed.set_image(url=F[str(ctx.guild.id)]['Shop'][str(Command).lower()]['url'])

            # LP.get_item(Server=str(ctx.guild.id), Player=str(ctx.author.id), Command_Name_Item=Command.lower(), Quantidade=Quantidade)

            msg = await ctx.send(embed=Embed)

            await msg.add_reaction('✅')
            await msg.add_reaction('❌')

            reaction, user = await self.bot.wait_for('reaction_add',timeout=30, check=lambda reaction, user: user.id == ctx.author.id)

            if str(reaction.emoji) == '✅':
                Lb = LPck.get_item(Server=str(ctx.guild.id), Player=str(ctx.author.id), Command_Name_Item=Command.lower(), Quantidade=Quantidade)
                if Lb:
                    await ctx.reply('Pronto, o item já está em seu invetário')

                elif Lb == False:
                    await ctx.reply('Pera pera, lê falta dinheiro')

            elif str(reaction.emoji) == '❌':
                await ctx.reply('Okok, você cancelou à compra')

def setup(bot):
    bot.add_cog(New_item(bot))