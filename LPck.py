import json
from time import sleep
import discord, math

def load_json(Name):
    with open(f'{Name}', 'r', encoding='utf-8') as F:
        return json.load(F)

def create_json_default(Server: str=None, Player: str=None):
    Name='Json/Server.json'

    F = load_json(Name=Name)

    if Server != None:
        F[str(Server)] = {}
        F[str(Server)]['Commaand'] = {}
        F[str(Server)]['Commaand']['Embed'] = {}
        F[str(Server)]['Commaand']['Message'] = {}
        F[str(Server)]['Shop'] = {}
        F[str(Server)]['Settings'] = {}

        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

    elif Player != None:
        Name = 'Json/Players.json'
        F = load_json(Name=Name)


        F[str(Server)] = {}
        F[str(Server)][str(Player)] = {}
        F[str(Server)][str(Player)]['inv'] = {}
        F[str(Server)][str(Player)]['status'] = {}
        F[str(Server)][str(Player)]['config'] = {}
        F[str(Server)][str(Player)]['config']['lembrete']  = {}
        F[str(Server)][str(Player)]['config']['baner'] = 'Img/2.png'
        F[str(Server)][str(Player)]['status']['xp'] = 0
        F[str(Server)][str(Player)]['status']['level'] = 1
        F[str(Server)][str(Player)]['status']['level-multiplicado'] = 100
        F[str(Server)][str(Player)]['status']['level_final'] = (int(F[str(Server)][str(Player)]['status']['level'] + 2) * int(F[str(Server)][str(Player)]['status']['level-multiplicado']))
        F[str(Server)][str(Player)]['status']['money'] = 7500

        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

def create_player_defaukt(Server, Player):
    Name = 'Json/Players.json'
    F = load_json(Name)
    
    F[str(Server)][str(Player)] = {}
    F[str(Server)][str(Player)]['inv'] = {}
    F[str(Server)][str(Player)]['status'] = {}
    F[str(Server)][str(Player)]['config'] = {}
    F[str(Server)][str(Player)]['config']['lembrete']  = {}
    F[str(Server)][str(Player)]['config']['baner'] = 'Img/2.png'
    F[str(Server)][str(Player)]['status']['xp'] = 0
    F[str(Server)][str(Player)]['status']['level'] = 1
    F[str(Server)][str(Player)]['status']['level-multiplicado'] = 100
    F[str(Server)][str(Player)]['status']['level_final'] = (int(F[str(Server)][str(Player)]['status']['level'] + 2) * int(F[str(Server)][str(Player)]['status']['level-multiplicado']))
    F[str(Server)][str(Player)]['status']['money'] = 7500

    with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

def set_xp(Server, Player, xp: int=0):
    Name = 'Json/Players.json'
    F = load_json(Name=Name)
    
    if not Server in F:
        create_json_default(Server=Server, Player=Player)
        sleep(2)

    if not Player in F[str(Server)]:
        create_player_defaukt(Server=Server, Player=Player)

    xp_pl = xp
    Level = F[str(Server)][str(Player)]['status']['level']
    Lvbrun = F[str(Server)][str(Player)]['status']["level-multiplicado"]
    Lvrun = F[str(Server)][str(Player)]['status']['level_final']
    Lvrun = (int(Level + 2)) * Lvbrun

    if xp_pl > Lvrun and Level < 500:
        while xp_pl >= Lvrun and Level < 500:
            Level += 1
            Lvbrun += 50
            Lvrun = (int(Level + 2)) * Lvbrun

    elif xp_pl < Lvrun and Level > 1:
        while xp_pl < Lvrun and Level > 1:
            Level -= 1
            Lvbrun -= 50
            Lvrun = (int(Level + 2)) * Lvbrun
                            
    if xp_pl == Lvrun:
        Level += 1
        Lvbrun += 50
        Lvrun = (int(Level + 2)) * Lvbrun

    F[str(Server)][str(Player)]['status']['xp'] = xp_pl
    F[str(Server)][str(Player)]['status']['level'] = Level
    F[str(Server)][str(Player)]['status']['level-multiplicado'] = Lvbrun
    F[str(Server)][str(Player)]['status']['level_final'] = Lvrun

    with open(Name, 'w') as H:
        json.dump(F, H, indent=2)

def set_lv(Server, Player, level: int=1):
    Name = 'Json/Players.json'
    F = load_json(Name=Name)
    
    if not Server in F:
        create_json_default(Server=Server, Player=Player)
        sleep(2)

    if not Player in F[str(Server)]:
        create_player_defaukt(Server=Server, Player=Player)

    xp_pl = F[str(Server)][str(Player)]['status']['xp']
    Level = F[str(Server)][str(Player)]['status']['level']
    Lvbrun = F[str(Server)][str(Player)]['status']["level-multiplicado"]
    Lvrun = F[str(Server)][str(Player)]['status']['level_final']

    Lv = level
    Lvrun = (int(Level + 2)) * Lvbrun

    if Lv > Level and Lv < 500:
        while Lv > Level and Level < 500:
            Level += 1
            xp_pl = Lvrun
            Lvbrun += 50
            Lvrun = (int(Level + 2)) * Lvbrun

    elif Lv < Level and Lv < 500:
        while Lv < Level and Level > 1:
            Level -= 1
            Lvbrun -= 50
            Lvrun = (int(Level + 2)) * Lvbrun
            xp_pl = Lvrun
                            
    if xp_pl == Lvrun:
        Level += 1
        Lvbrun += 50
        Lvrun = (int(Level + 2)) * Lvbrun

    F[str(Server)][str(Player)]['status']['xp'] = xp_pl
    F[str(Server)][str(Player)]['status']['level'] = Level
    F[str(Server)][str(Player)]['status']['level-multiplicado'] = Lvbrun
    F[str(Server)][str(Player)]['status']['level_final'] = Lvrun

    with open(Name, 'w') as H:
        json.dump(F, H, indent=2)

def set_coin(Server, Player, coin: int=7500):
    Name = 'Json/Players.json'
    F = load_json(Name=Name)
    
    if not Server in F:
        create_json_default(Server=Server, Player=Player)
        sleep(1)

    F[str(Server)][str(Player)]['status']['money'] = coin

    with open(Name, 'w') as H:
        json.dump(F, H, indent=2)

def new_item(Server, Name_Command: str=None, Name: str=None, description: str='', Sell: int=None, url: str=None):
    if Name_Command != None and Name != None and Sell != None:
        Name_ = 'Json/Server.json'
        F = load_json(Name_)

    if not Server in F:
        create_json_default(Server=Server)

    F[str(Server)]['Shop'][str(Name_Command.lower())] = {}
    F[str(Server)]['Shop'][str(Name_Command.lower())]['name'] = Name
    F[str(Server)]['Shop'][str(Name_Command.lower())]['description'] = description
    F[str(Server)]['Shop'][str(Name_Command.lower())]['sell'] = int(Sell)
    F[str(Server)]['Shop'][str(Name_Command.lower())]['url'] = url

    with open(Name_, 'w') as H:
        json.dump(F, H, indent=2)


def get_item(Server, Player, Command_Name_Item, Quantidade: int=1):
    Name_Player = 'Json/Players.json'
    Name_Server = 'Json/Server.json'

    F = load_json(Name_Server)
    H = load_json(Name_Player)

    if not Server in F:
        create_json_default(Server=Server, Player=Player)

    if not str(Command_Name_Item.lower()) in F[str(Server)]['Shop']:
        print('Item não encontrado!')

    else:
        Custo = F[str(Server)]['Shop'][str(Command_Name_Item.lower())]['sell'] * Quantidade
        Money = H[str(Server)][str(Player)]['status']['money']
        Nome_item = F[str(Server)]['Shop'][str(Command_Name_Item.lower())]['name']
        
        if Custo * Quantidade > Money:
            return False

        elif Money >= Custo * Quantidade:
            Money = Money - Custo * Quantidade
            if str(Command_Name_Item).lower() in H[str(Server)][str(Player)]['inv']:
                H[str(Server)][str(Player)]['inv'][str(Command_Name_Item).lower()]['quantidade'] += Quantidade

            else:
                H[str(Server)][str(Player)]['inv'][str(Command_Name_Item).lower()] = {}        
                H[str(Server)][str(Player)]['inv'][str(Command_Name_Item).lower()]['name'] = Nome_item
                H[str(Server)][str(Player)]['inv'][str(Command_Name_Item).lower()]['quantidade'] = Quantidade

            H[str(Server)][str(Player)]['status']['money'] = Money

            with open(Name_Player, 'w') as F:
                json.dump(H, F, indent=2)
            
            return True

def get_player(Server, Player):
    Name = 'Json/Players.json'
    F = load_json(Name)
    
    if not Player in F[str(Server)]:
        create_player_defaukt(str(Server), str(Player))
        sleep(2)
    
    if Player in F[str(Server)]:
        return F[str(Server)][str(Player)]

def get_all_itens(Server):
    Name = 'Json/Server.json'
    F = load_json(Name)
    Kk = []

    if not Server in F:
        create_json_default(Server=Server)

    if Server in F:
        for i in F[str(Server)]['Shop']:
            Kk.append(f"`{F[str(Server)]['Shop'][str(i)]['name']} **Custo: {F[str(Server)]['Shop'][str(i)]['sell']}**`")

        return '\n'.join(Kk)

def remove_item_store(Server, Item):
    pass

def Inventory(Server, User):
    Name = 'Json/Players.json'
    Name_ = 'Json/Server.json'
    
    F = load_json(Name)
    H = load_json(Name_)
    Kk = []

    inventory = F[str(Server)][str(User)]['inv']

    for i in inventory:
        if not inventory[str(i)]['quantidade'] == 0:
            Kk.append(inventory[str(i)]['name'])

    return '\n'.join(Kk), Kk

# def new_Command(Command_Name): 

def command_new_message(Guild, Name_Command):
    
    with open('Json/Server.json', 'r') as F:
        F = json.load(F)

    Name_Command = str(Name_Command).replace(' ', '-')

    Msg = 'Message'

    if not str(Name_Command).lower() in F[str(Guild)]['Commaand'][Msg]:
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()] = {}
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['config'] = {}
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['content'] = {}

        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['config']['Xp'] = False
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['config']['Money'] = False
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['config']['Task'] = False
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['config']['Item'] = False

        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['content']['Message'] = {}
        F[str(Guild)]['Commaand'][Msg][str(Name_Command).lower()]['content']['Message']['content'] = []

        with open('Json/Server.json', 'w') as H:
            json.dump(F, H, indent=2)

        return True

    else:
        return False

def add_embed(Guild: str=None, Name_Command: str=None, Title: str=None, description=str, Embed: bool=False):
    
    Name = 'Json/Server.json'
    F = load_json(Name)
    
    if Name_Command in F[str(Guild)]['Commaand']['Embed']:
        Embed = discord.Embed(
            title=Title,
            description=description,
            colour=7419530
        )

        Name_Command = str(Name_Command).replace(' ', '-')

        F[str(Guild)]['Commaand']['Embed'][str(Name_Command).lower()]['content']['Message']['content'].append(Embed)
        
        
        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

        return True

    else:
        return False

def add_messsage(Guild, Name_Command, content):
    Name = 'Json/Server.json'
    F = load_json(Name)
    
    if Name_Command in F[str(Guild)]['Commaand']['Message']:
        F[str(Guild)]['Commaand']['Message'][str(Name_Command).lower()]['content']['Message']['content'].append(str(content))

        with open(Name, 'w') as H:
            json.dump(F, H, indent=2)

        return True

    else:
        return False

def num_fmt(num):
    i_offset = 15 # change this if you extend the symbols!!!
    prec = 3
    fmt = '.{p}g'.format(p=prec)
    symbols = ['Y', 'T', 'G', 'M', 'k', '', 'm', 'u', 'n']

    e = math.log10(abs(num))
    if e >= i_offset + 3:
        return '{:{fmt}}'.format(num, fmt=fmt)
    for i, sym in enumerate(symbols):
        e_thresh = i_offset - 3 * i
        if e >= e_thresh:
            return '{:{fmt}}{sym}'.format(num/10.**e_thresh, fmt=fmt, sym=sym)
    
    return '{:{fmt}}'.format(num, fmt=fmt)

Name = 'Json/P.json'
F = load_json(Name)
