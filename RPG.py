import discord
from discord.ext import commands

def Roles_Verification(User, Role: list=None, u: str="None"):

    for i in User.roles:
        if i.id in Role or i.id in [971804611402948658, 971804613449773066, 976573383305203733, 974336093757538425] and u == 'npc':
            return True

def Message_Respiração(Modo, Nome_Forma: str=None, Geral: str=None, Forma: str=None, Dano: str=None, Fôlego: str=None, alert: str=None, url: str=None, Humano=False, Oni=False, Híbrido=False, user=None, npc: str='None'):
        
        if Humano or Híbrido:
            Embed = discord.Embed(
            title=Nome_Forma,
                description= f'{Geral}\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
                colour=3426654
            )

            if Modo == 1:
                Embed.add_field(name=Forma, value=f'•「❤️」**{Dano}** De Dano\n•「💨」**{Fôlego}** De Fôlego')

                Embed.set_image(url=url)
                
                return  Embed

            elif Modo == 2:
                Embed.add_field(name=Forma, value=f'•「❤️」**{Dano}**\n•「💨」**{Fôlego}** De Fôlego\n•「⚠️」{alert}')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 3:
                Embed.add_field(name=Forma, value=f'•「⚠️」{alert}\n•「💨」**{Fôlego}** De Fôlego')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 4:
                Embed.add_field(name=Forma, value=f'•「❤️」{Dano}\n•「💨」**{Fôlego}** De Fôlego')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 5:
                Embed.add_field(name=Forma, value=f'{Dano}')

                Embed.set_image(url=url)

                return Embed

        elif Oni:
            Embed = discord.Embed(
           title=Nome_Forma,
            description= f'{Geral}\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
            colour=3426654
        )

            if Modo == 1:
                Embed.add_field(name=Forma, value=f'•「❤️」**{Dano}** De Dano\n•「🩸」**{Fôlego}** De Sangue')

                Embed.set_image(url=url)
                
                return  Embed

            elif Modo == 2:
                Embed.add_field(name=Forma, value=f'•「❤️」**{Dano}**\n•「🩸」**{Fôlego}** De Sangue\n•「⚠️」{alert}')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 3:
                Embed.add_field(name=Forma, value=f'•「⚠️」{alert}\n•「🩸」**{Fôlego}** De Sangue')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 4:
                Embed.add_field(name=Forma, value=f'•「❤️」{Dano}\n•「🩸」**{Fôlego}** De Sangue')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 5:
                Embed.add_field(name=Forma, value=f'{Dano}'.replace('Fôlego', 'Sangue').replace('fôlego', 'Sangue').replace('💨', '🩸'))

                Embed.set_image(url=url)

                return Embed

        elif user and npc == 'npc':
            Embed = discord.Embed(
            title=Nome_Forma,
                description= f'{Geral}\n\n**✦ ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ・あ・⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ✦**',
                colour=3426654
            )

            if Modo == 1:
                Embed.add_field(name=Forma, value=f'•「❤️」**{Dano}** De Dano\n•「💨」**{Fôlego}** De Fôlego')

                Embed.set_image(url=url)
                
                return  Embed

            elif Modo == 2:
                Embed.add_field(name=Forma, value=f'•「❤️」**{Dano}**\n•「💨」**{Fôlego}** De Fôlego\n•「⚠️」{alert}')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 3:
                Embed.add_field(name=Forma, value=f'•「⚠️」{alert}\n•「💨」**{Fôlego}** De Fôlego')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 4:
                Embed.add_field(name=Forma, value=f'•「❤️」{Dano}\n•「💨」**{Fôlego}** De Fôlego')

                Embed.set_image(url=url)

                return Embed

            elif Modo == 5:
                Embed.add_field(name=Forma, value=f'{Dano}')

                Embed.set_image(url=url)

                return Embed


    