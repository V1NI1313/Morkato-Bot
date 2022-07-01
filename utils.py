from textwrap import indent
import discord
import json
from discord.ext import commands

Name = 'Json/P.json'
F = load_json(Name)

def New_User(Server: discord.Guild, Player: discord.Member):
    while True:
        try:
            F[str(Server.id)][str(Player.id)] = {}
            F[str(Server.id)][str(Player.id)]['inv'] = {}
            F[str(Server.id)][str(Player.id)]['status'] = {}
            F[str(Server.id)][str(Player.id)]['config'] = {}
            F[str(Server.id)][str(Player.id)]['config']['lembrete']  = {}
            F[str(Server.id)][str(Player.id)]['config']['baner'] = 'Img/2.png'
            F[str(Server.id)][str(Player.id)]['status']['xp'] = 0
            F[str(Server.id)][str(Player.id)]['status']['level'] = 1
            F[str(Server.id)][str(Player.id)]['status']['level-multiplicado'] = 100
            F[str(Server.id)][str(Player.id)]['status']['level_final'] = (int(F[str(Server.id)][str(Player.id)]['status']['level'] + 2) * int(F[str(Server.id)][str(Player.id)]['status']['level-multiplicado']))
            F[str(Server.id)][str(Player.id)]['status']['money'] = 7500

            with open(Name, 'w') as H:
                json.dump(F, H, indent=2)

            break

        except:
            F[str(Server.id)] = {}

            with open(Name, 'w') as H:
                json.dump(F, H, indent=2)


class Get_User:
    def __init__(self, Guild: discord.Guild=None, User: discord.Member=None):
        while True:
            try:
                self.name = User.name
                self.id = User.id
                self.url = User.avatar_url_as(size=256)
                self.xp = F[str(Guild.id)][str(User.id)]['status']['xp']
                self.lv = F[str(Guild.id)][str(User.id)]['status']['level']
                self.lvrun = F[str(Guild.id)][str(User.id)]['status']['level_final']
                self.lvbrun = F[str(Guild.id)][str(User.id)]['status']['level-multiplicado']
                self.money = F[str(Guild.id)][str(User.id)]['status']['money']
                self.banner = F[str(Guild.id)][str(User.id)]['config']['baner']

                # ==============> Guida <==================
                
                self.guild_name = Guild.name
                self.guild_id = Guild.id
                
                break

            except:
                New_User(Server=Guild, Player=User)


    def set_xp(self, xp: int=0):
        
        self.xp = xp
        self.lv = F[str(self.guild_id)][str(self.id)]['status']['level']
        self.lvbrun = F[str(self.guild_id)][str(self.id)]['status']['level-multiplicado']
        self.lvrun = (int(self.lv + 2) * int(self.lvbrun))

        while self.xp > self.lvrun and self.lv < 500:
            self.lv += 1
            self.lvbrun += 50
            self.lvrun = (int(self.lv + 2)) * self.lvbrun

        while self.xp < self.lvrun and self.lv > 1:
            self.lv -= 1
            self.lvbrun -= 50
            self.lvrun = (int(self.lv + 2)) * self.lvbrun
                                
        if self.xp == self.lvrun:
            self.lv += 1
            self.lvbrun += 50
            self.lvrun = (int(self.lv + 2)) * self.lvbrun

        F[str(self.guild_id)][str(self.id)]['status']['xp'] = self.xp
        F[str(self.guild_id)][str(self.id)]['status']['level'] = self.lv
        F[str(self.guild_id)][str(self.id)]['status']['level-multiplicado'] = self.lvbrun
        F[str(self.guild_id)][str(self.id)]['status']['level_final'] = self.lvrun

        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

    def set_lv(self, Level: int):
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

        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

    def set_money(self, money: str):
        self.money = int(money.lower().replace('k', '000').replace('m', '000000'))

        F[str(self.guild_id)][str(self.id)]['status']['mone'] = self.money

        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

F = load_json('Json/Sla.json')

class Guild:
    def __init__(self, Guild: discord.Guild):
        while True:
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
        F[str(self.id)]['Item'][str(Name)] = {}
        F[str(self.id)]['Item'][str(Name)]['content'] = {}
        F[str(self.id)]['Item'][str(Name)]['content']['title'] = None
        F[str(self.id)]['Item'][str(Name)]['content']['decription'] = 'None'
        F[str(self.id)]['Item'][str(Name)]['content']['tumb'] = None
        F[str(self.id)]['Item'][str(Name)]['content']['url'] = None

        F[str(self.id)]['loja'][str(Name)] = {}
        F[str(self.id)]['loja'][str(Name)]['custo'] = 0
        
        with open('Json/Sla.json', 'w') as H:
            json.dump(F, H, indent=2)

    def New_Command(self, name, embed: bool):
        if embed:
            while True:
                try:
                    F[str(self.id)]['commands']['embed'][f'{o}{name}'] = {}
                    F[str(self.id)]['commands']['embed'][f'{o}{name}']['config'] = {}
                    F[str(self.id)]['commands']['embed'][f'{o}{name}']['content'] = {}

                    F[str(self.id)]['commands']['embed'][f'{o}{name}']['content']['title'] = None
                    F[str(self.id)]['commands']['embed'][f'{o}{name}']['content']['description'] = 'None'
                    F[str(self.id)]['commands']['embed'][f'{o}{name}']['content']['tumb'] = False
                    F[str(self.id)]['commands']['embed'][f'{o}{name}']['content']['url'] = False

                    with open('Json/Sla.json', 'w') as H:
                        json.dump(F, H, indent=2)

                    break

                except:
                    F[str(self.id)]['commands']['embed'] = {}

                    with open('Json/Sla.json', 'w') as H:
                        json.dump(F, H, indent=2)

    def Item_Info(self, Name):
        if Name in self.itens:
            self.title = F[str(self.id)]['Item'][str(Name)]['content']['title']
            self.description = F[str(self.id)]['Item'][str(Name)]['content']['tdescription']
            self.tumb = F[str(self.id)]['Item'][str(Name)]['content']['tumb']
            self.url = F[str(self.id)]['Item'][str(Name)]['content']['url']

            self.custo = F[str(self.id)]['loja'][str(Name)]['custo']
            
