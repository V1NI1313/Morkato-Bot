import discord
import json

def New_User(Server: discord.Guild, Player: discord.Member):
    while True:
        try:
            with open('Json/P.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            F[str(Server.id)][str(Player.id)] = {}
            F[str(Server.id)][str(Player.id)]['inv'] = {}
            F[str(Server.id)][str(Player.id)]['status'] = {}
            F[str(Server.id)][str(Player.id)]['config'] = {}
            F[str(Server.id)][str(Player.id)]['config']['lembrete']  = {}
            F[str(Server.id)][str(Player.id)]['config']['baner'] = 'Img/2.png'
            F[str(Server.id)][str(Player.id)]['config']['noti'] = True
            F[str(Server.id)][str(Player.id)]['status']['xp'] = 0
            F[str(Server.id)][str(Player.id)]['status']['level'] = 1
            F[str(Server.id)][str(Player.id)]['status']['level_final'] = int(F[str(Server.id)][str(Player.id)]['status']['level'] + 1) * (F[str(Server.id)][str(Player.id)]['status']['level'] * 100)
            F[str(Server.id)][str(Player.id)]['status']['money'] = 7500

            break

        except:
            F[str(Server.id)] = {}

            with open('Json/P.json', 'w') as H:
                json.dump(F, H, indent=2)

    with open('Json/P.json', 'w') as H:
        json.dump(F, H, indent=2)

class Get_User:
    def __init__(self, Guild: discord.Guild=None, User: discord.Member=None):
        self.gui = Guild
        self.user = User

        self.name = User.name
        self.id = User.id
        self.url = User.avatar_url_as(size=256)

        self.guild_name = Guild.name
        self.guild_id = Guild.id

        while True:
            with open('Json/P.json', 'r') as F:
                F = json.load(F)

            try:
                self.xp = F[str(Guild.id)][str(User.id)]['status']['xp']
                self.lv = F[str(Guild.id)][str(User.id)]['status']['level']
                self.lvrun = F[str(Guild.id)][str(User.id)]['status']['level_final']
                self.noti = F[str(Guild.id)][str(User.id)]['config']['noti']
                # self.lvbrun = F[str(Guild.id)][str(User.id)]['status']['level-multiplicado']
                self.money = F[str(Guild.id)][str(User.id)]['status']['money']
                self.banner = F[str(Guild.id)][str(User.id)]['config']['baner']
                self.inv = F[str(Guild.id)][str(User.id)]['inv']
                
                break

            except:
                New_User(Server=Guild, Player=User)


    def set_xp(self, xp: int=0, pop_up: bool=False):
        with open('Json/P.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        G = False
        
        while xp > int(self.lv + 1) * (self.lv * 100):
            self.lv += 1
            self.lvrun = int(self.lv + 1) * (self.lv * 100)

        if self.lv > F[str(self.guild_id)][str(self.id)]['status']['level'] and pop_up:
            G = True

        F[str(self.guild_id)][str(self.id)]['status']['level'] = self.lv
        F[str(self.guild_id)][str(self.id)]['status']['level_final'] = self.lvrun
        F[str(self.guild_id)][str(self.id)]['status']['xp'] = xp
        
        with open('Json/P.json', 'w') as H:
            json.dump(F, H, indent=2)

        return G

    def set_lv(self, Level: int):
        with open('Json/P.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        self.xp = F[str(self.guild_id)][str(self.id)]['status']['xp']
        self.lv = F[str(self.guild_id)][str(self.id)]['status']['level']
        self.lvbrun = F[str(self.guild_id)][str(self.id)]['status']['level-multiplicado']
        self.lvrun = (int(self.lv + 2) * int(self.lvbrun))

        while Level > self.lv and Level < 500:
            self.lv += 1
            self.xp = self.lvrun
            self.lvbrun += 50
            self.lvrun = (int(Level + 2)) * self.lvbrun

        while Level < self.lv and Level >= 1:
            self.lv -= 1
            self.xp = self.lvrun
            self.lvbrun -= 50
            self.lvrun = (int(Level + 2)) * self.lvbrun

        if self.xp == self.lvrun:
            self.lv += 1
            self.lvbrun += 50
            self.lvrun = (int(self.lv + 2)) * self.lvbrun

        F[str(self.guild_id)][str(self.id)]['status']['xp'] = self.xp
        F[str(self.guild_id)][str(self.id)]['status']['level'] = self.lv
        F[str(self.guild_id)][str(self.id)]['status']['level-multiplicado'] = self.lvbrun
        F[str(self.guild_id)][str(self.id)]['status']['level_final'] = self.lvrun

        with open('Json/P.json', 'w') as H:
            json.dump(F, H, indent=2)

    def set_money(self, money: str):
        with open('Json/P.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        self.money = int(money.lower().replace('k', '000').replace('m', '000000'))

        F[str(self.guild_id)][str(self.id)]['status']['mone'] = self.money

        with open('Json/P.json', 'w') as H:
            json.dump(F, H, indent=2)

    def Usar(self, Name, Q: int=1):
        with open('Json/P.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        Guil = Guild(Guild=self.gui)
        Item = Guil.Item_Info(Name=Name)

        if Item.verification == True and Name in F[str(self.guild_id)][str(self.id)]['inv']:
            if not F[str(self.guild_id)][str(self.id)]['inv'][str(Name)] < Q:
                F[str(self.guild_id)][str(self.id)]['inv'][str(Name)] -= Q

                with open('Json/P.json', 'w') as H:
                    json.dump(F, H, indent=2)

                return True

            else:
                if F[str(self.guild_id)][str(self.id)]['inv'][str(Name)] == 0:
                    del F[str(self.guild_id)][str(self.id)]['inv'][str(Name)]

                    with open('Json/P.json', 'w') as H:
                        json.dump(F, H, indent=2)

                return False

        else:
            return False

    def Get_Item(self, Name, Q: int=1):
        Item = Guild(self.gui).Item_Info(Name=Name)

        with open('Json/P.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        if Item.verification:
            if not Name in self.inv:
                F[str(self.guild_id)][str(self.id)]['inv'][str(Name)] = Q

            if Name in self.inv:
                F[str(self.guild_id)][str(self.id)]['inv'][str(Name)] += Q

            with open('Json/P.json', 'w') as H:
                json.dump(F, H, indent=2)

            return True
        
        elif not Item.verification:
            return False

    def Usar_Command(self, Name):
        with open('Json/P.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        Command = Guild(Guild=self.gui).Command_Info(command=Name)

        if Command.verification: 
            Embed = discord.Embed(
                title=str(Command.title),
                description=str(Command.description),
                colour=0x9B59B6
            )

            if not Command.url == None:
                Embed.set_image(url=Command.url)

            if Command.config_itens == {}:
                return Embed

            elif not Command.config_itens == {}:
                for i in Command.config_itens:
                    In = int(Command.config_itens[str(i)])
                    i = i

                if not str(i) in self.inv and In > 0:
                    F[str(self.guild_id)][str(self.id)]['inv'][str(i)] = In

                    with open('Json/P.json', 'w') as H:
                        json.dump(F, H, indent=2)

                    return Embed
                    
                if str(i) in self.inv:
                    if F[str(self.guild_id)][str(self.id)]['inv'][str(i)] == 0:
                        del F[str(self.guild_id)][str(self.id)]['inv'][str(i)]

                        with open('Json/P.json', 'w') as H:
                            json.dump(F, H, indent=2)

                        return

                    elif In > 0:
                        F[str(self.guild_id)][str(self.id)]['inv'][str(i)] += In

                    elif F[str(self.guild_id)][str(self.id)]['inv'][str(i)] >= In * -1:
                        F[str(self.guild_id)][str(self.id)]['inv'][str(i)] -= In * -1

                    with open('Json/P.json', 'w') as H:
                        json.dump(F, H, indent=2)
                    
                    return Embed

class Guild:
    def __init__(self, Guild: discord.Guild):
        while True:
            with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            try:
                self.name = str(Guild.name)
                self.id = Guild.id
                self.settings = F[str(self.id)]['settings']
                self.loja = F[str(self.id)]['loja']
                self.commands = F[str(Guild.id)]['commands']
                self.itens = F[str(Guild.id)]['Item']

                break

            except:
                F[str(self.id)] = {}
                F[str(self.id)]['settings'] = {}
                F[str(self.id)]['loja'] = {}
                F[str(self.id)]['commands'] = {}
                F[str(self.id)]['Item'] = {}

                with open('Json/Sla.json', 'w') as H:
                    json.dump(F, H, indent=2)

    def New_Item(self, Name):
        with open('Json/Sla.json', 'r') as F:
            F = json.load(F)

        F[str(self.id)]['Item'][str(Name)] = {}
        F[str(self.id)]['Item'][str(Name)]['config'] = {}
        F[str(self.id)]['Item'][str(Name)]['content'] = {}
        F[str(self.id)]['Item'][str(Name)]['content']['title'] = None
        F[str(self.id)]['Item'][str(Name)]['content']['description'] = 'None'
        F[str(self.id)]['Item'][str(Name)]['content']['tumb'] = None
        F[str(self.id)]['Item'][str(Name)]['content']['url'] = None
        F[str(self.id)]['Item'][str(Name)]['config']['command_vinculate'] = None
        
        with open('Json/Sla.json', 'w') as H:
            json.dump(F, H, indent=2)

    def New_Command(self, Name):
        if not Name in self.commands:
            with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            F[str(self.id)]['commands'][str(Name)] = {}
            F[str(self.id)]['commands'][str(Name)]['config'] = {}
            F[str(self.id)]['commands'][str(Name)]['config']['item'] = {}
            F[str(self.id)]['commands'][str(Name)]["content"] = {}
            F[str(self.id)]['commands'][str(Name)]["content"]['title'] = None
            F[str(self.id)]['commands'][str(Name)]["content"]['description'] = None
            F[str(self.id)]['commands'][str(Name)]["content"]['tumb'] = None
            F[str(self.id)]['commands'][str(Name)]["content"]['url'] = None
            
            with open('Json/Sla.json', 'w') as H:
                json.dump(F, H, indent=2)

            return True

        elif Name in self.commands:
            return False

    class Item_info:
        def __init__(self, Guild: int, Name):
            with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            self.name = Name
            self.id = Guild

            if Name in F[str(Guild)]['Item']:
                self.title = F[str(Guild)]['Item'][str(Name)]['content']['title']
                self.description = F[str(Guild)]['Item'][str(Name)]['content']['description']
                self.tumb = F[str(Guild)]['Item'][str(Name)]['content']['tumb']
                self.url = F[str(Guild)]['Item'][str(Name)]['content']['url']
                self.command_vin = F[str(Guild)]['Item'][str(Name)]['config']['command_vinculate']
                self.itens = F[str(Guild)]['Item']

                self.verification = True
                self.Embed = discord.Embed(
                    title=str(self.title),
                    description=str(self.description),
                    colour=0x9B59B6
                )

            else:
                self.verification = False

        def edit(self, **args):
            with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            if 'title' in args and 'description' in args and 'tumb' in args and 'url' in args:
                if args['title'] == None:
                    args['title'] = self.title

                if args['description'] == None:
                    args['description'] = self.description

                if args['tumb'] == None:
                    args['tumb'] = self.tumb

                if args['url'] == None:
                    args['url'] = self.url
                
                F[str(self.id)]['Item'][str(self.name)]["content"] = args

                with open('Json/Sla.json', 'w') as H:
                    json.dump(F, H, indent=2)

    class Command_info:
        def __init__(self, command, id):
            with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            self.itens = F[str(id)]['commands']
            self.id = id
            self.name = command

            if command in self.itens:
                for i in F[str(self.id)]['commands'][str(command)]['config']['item']: i = i

                self.config = F[str(self.id)]['commands'][str(command)]['config']
                self.config_itens = F[str(self.id)]['commands'][str(command)]['config']['item']
                self.title = F[str(self.id)]['commands'][str(command)]["content"]['title']
                self.description = F[str(self.id)]['commands'][str(command)]["content"]['description']
                self.item_vinculate = i
                self.tumb = F[str(self.id)]['commands'][str(command)]["content"]['tumb']
                self.url = F[str(self.id)]['commands'][str(command)]["content"]['url']

                self.Embed_Info = discord.Embed(
                    title='',
                    description=f'A descrição do seu comando é:\n\n**```{self.description}```**\n\nA imagem do seu item é:\n\n**```{self.url}```**\n\n A tumb do seu comando é:\n\n**```{self.tumb}```**\nItem Vinculado do seu comando é:\n\n**```{self.item_vinculate}```**',
                    colour=0x9B59B6
                )
                self.verification = True

            else:
                self.verification = False

        def edit(self, **args):
            with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                F = json.load(F)

            if 'title' in args and 'description' in args and 'tumb' in args and 'url' in args:
                if args['title'] == None:
                    args['title'] = self.title

                if args['description'] == None:
                    args['description'] = self.description

                if args['tumb'] == None:
                    args['tumb'] = self.tumb

                if args['url'] == None:
                    args['url'] = self.url
                
                F[str(self.id)]['commands'][str(self.name)]["content"] = args

                with open('Json/Sla.json', 'w') as H:
                    json.dump(F, H, indent=2)


    def Item_Info(self, Name):
        return self.Item_info(Guild=self.id, Name=Name)

    def Command_Info(self, command):
        return self.Command_info(command=command, id=self.id)

    def Vincular_Item(self, command, item, Q: int=1):
        with open('Json/Sla.json', 'r', encoding='utf-8') as F:
            F = json.load(F)

        Command = self.Command_Info(command=command)
        Item = self.Item_Info(Name=item)

        if not Command.verification and not Item.verification:
            return False

        elif Command.verification and Item.verification:
            while True:
                with open('Json/Sla.json', 'r', encoding='utf-8') as F:
                    F = json.load(F)
                
                try:
                    F[str(self.id)]['commands'][str(command)]['config']['item'][str(item)] = Q
                    F[str(self.id)]['Item'][str(item)]['config']['command_vinculate'] = command

                    with open('Json/Sla.json', 'w') as H:
                        json.dump(F, H, indent=2)

                        return True       

                except:
                    F[str(self.id)]['commands'][str(command)]['config']['item'] = {}

                    with open('Json/Sla.json', 'w') as H:
                        json.dump(F, H, indent=2)
