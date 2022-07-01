import datetime, json

def Time(Guld: str=None, Autor: str=None):
    with open('Json/Players.json', 'r') as F:
        H = json.load(F)

    with open('Json/Server.json', 'r') as F:
        F = json.load(F)

    # if F[str(Guld)]["Commands"][str(Command)]['Time'] == True:

        now = datetime.datetime.now()

        Data = now.day
        Hora = now.hour
        Minuto = now.minute

        if H[str(Guld)][str(Autor)]['status']['data'] == 'None':
            Minuto = now.minute

            """        while Minuto >= 60:
                Hora += 1
                Minuto -= 60

                if Hora >= 24:
                    Hora = 0
                    Data += 1

            """

            H[str(Guld)][str(Autor)]['status']['data'] = Data
            H[str(Guld)][str(Autor)]['status']['minuto'] = Minuto
            H[str(Guld)][str(Autor)]['status']['hora'] = Hora


            with open('Json/Players.json', 'w') as F:
                json.dump(H, F, indent=4)

            return 1

        Minuto_último_Treino = H[str(Guld)][str(Autor)]['status']['minuto'] + 60
        Hora_último_Treino = H[str(Guld)][str(Autor)]['status']['hora']
        Dia_último_treino = H[str(Guld)][str(Autor)]['status']['data']


        while Minuto_último_Treino >= 60:
            Hora_último_Treino += 1
            Minuto_último_Treino -= 60

            if Hora_último_Treino > 23:
                Hora_último_Treino = 0
                Dia_último_treino += 1

            elif Dia_último_treino < now.day:
                Hora_último_Treino = now.hour - Hora_último_Treino

        if Minuto_último_Treino <= now.minute and Hora_último_Treino <= now.hour and Dia_último_treino <= now.day or Hora_último_Treino < now.hour and Dia_último_treino <= now.day or Dia_último_treino < now.day:

            H[str(Guld)][str(Autor)]['status']['data'] = Data
            H[str(Guld)][str(Autor)]['status']['minuto'] = Minuto
            H[str(Guld)][str(Autor)]['status']['hora'] = Hora


            with open('Json/Players.json', 'w') as F:
                json.dump(H, F, indent=4)

            return 1

        else:
            HoraGG = H[str(Guld)][str(Autor)]['status']['hora'] - Hora
            MinutoGG = H[str(Guld)][str(Autor)]['status']['minuto'] - Minuto

            if MinutoGG <= 0:
                HoraGG -= 1
                MinutoGG += 60

            return MinutoGG

    # else:
      #  return 1