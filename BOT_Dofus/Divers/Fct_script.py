from Divers import fonction_principal as Fct


def lire_zaap(script,listzaap):
    begin = False
    for i in script:
        if i == 'fin Zaap':
            break
        if i == 'Zaap':
            begin = True
        elif (begin):
            if(not(i in listzaap)):
                listzaap.append(i)
    return listzaap

def lire_path(path):
    textfile = open(path, "r")
    script = []
    while True:
        line = textfile.readline()
        if ((line == 'final\n') or (line == 'final')):
            break
        script.append(line[0:-1])
    return script

def lire_nom(script):
    return script[0]

def lire_script(script):
    begin = False
    action = []
    for i in script:
        if i == 'fin Action':
            break
        if i == 'Action':
            begin = True
        elif (begin):
            action.append(i)

    begin = False
    key = 0
    Dicto_ressource = {}
    actuel = {}
    for i in script:
        if i == 'fin Ressource':
            Dicto_ressource[key] = actuel
            break
        if i == 'Ressource':
            begin = True
        elif (i[0:3] == 'map') and begin:
            if key != 0:
                Dicto_ressource[key] = actuel
                actuel = {}
            keylist = i[4:].split(', ')
            key = (int(keylist[0]), int(keylist[1]))
        elif begin:
            itemlist = i.split(', ')
            actuel[(int(itemlist[1]), int(itemlist[2]))] = (int(itemlist[4]), int(itemlist[5]), int(itemlist[6]))

    begin = False
    first = True
    Tout_caverne = {}
    pos_caverne = {}
    pos_couleur = {}
    ressource_caverne_temp = {}
    ressource_caverne = {}
    couleur_caverne = {}
    pos = -1
    caverne_actuel = (0,0)
    for i in script:
        if i == 'fin Caverne':
            ressource_caverne[pos] = ressource_caverne_temp
            Tout_caverne[caverne_altuel] = [pos_caverne, couleur_caverne, pos_couleur, ressource_caverne]
            break
        if i == 'Caverne':
            begin = True
        elif(i[0:3] == 'New') and begin:
            if first:
                caverne_altuel = i[4:].split(', ')
                caverne_altuel = (int(caverne_altuel[0]), int(caverne_altuel[1]))
                first = False
                pos = -1
            else:
                ressource_caverne[pos] = ressource_caverne_temp
                Tout_caverne[caverne_altuel] = [pos_caverne, couleur_caverne, pos_couleur, ressource_caverne]
                pos_caverne = {}
                couleur_caverne = {}
                pos_couleur = {}
                ressource_caverne = {}
                ressource_caverne_temp = {}
                caverne_altuel = i[4:].split(', ')
                caverne_altuel = (int(caverne_altuel[0]),int(caverne_altuel[1]))
                pos = -1
        elif begin:
            if i[0:8] == 'position':
                ressource_caverne[pos] = ressource_caverne_temp
                pos = pos+1
                info = i.split(', ')
                pos_caverne[pos] = (int(info[1]),int(info[2]),int(info[3]),int(info[4]))
                couleur_caverne[pos] = (int(info[6]),int(info[7]),int(info[8]))
                pos_couleur[pos] = (int(info[10]),int(info[11]))
                ressource_caverne_temp = {}
            elif i[0:9] == 'ressource':
                itemlist = i.split(', ')
                ressource_caverne_temp[(int(itemlist[1]), int(itemlist[2]))] = (int(itemlist[4]), int(itemlist[5]), int(itemlist[6]))



    return action, Dicto_ressource, Tout_caverne


def run_action(action, Dicto_ressource, Dicto_zaap, Dicto_caverne, pause=[False]):
    bool_caverne = False
    pos_caverne = (0, 0)
    num_carte_caverne = 0
    for i in action:
        if i[0:5] == 'Go to':
            if bool_caverne:
                pos = i[6:]
                num_carte_caverne = Fct.Go_to_POS_Caverne(int(pos), Dicto_caverne[pos_caverne][0], Dicto_caverne[pos_caverne][1], Dicto_caverne[pos_caverne][2], num_carte_caverne, pause=pause)
            else:
                pos = i[6:].split(', ')
                NbSauf = int((len(pos) - 3)/6)
                sauf = {}
                for j in range(NbSauf):
                    sauf[(int(pos[j*6+3]), int(pos[j*6+4]))] = (int(pos[j*6+5]), int(pos[j*6+6]), int(pos[j*6+7]), int(pos[j*6+8]))
                Fct.Go_to_POS([int(pos[0]), int(pos[1])], sauf=sauf, pause=pause)
        if (i[0:6] == 'Sortie'):
            bool_caverne = False
            num_carte_caverne = 0
        if i[0:6] == 'Rentre':
            pos_caverne = tuple(Fct.MAP_POS())
            bool_caverne = True
            num_carte_caverne = 0
        if i[0:5] == 'Check':
            if bool_caverne:
                Fct.ressource(Dicto_caverne[pos_caverne][3][num_carte_caverne], pause=pause)
            else:
                now = tuple(Fct.MAP_POS())
                if now in Dicto_ressource:
                    Fct.ressource(Dicto_ressource[now], pause=pause)
        if i[0:4] == 'Zaap':
            Fct.zaap(i[5:], Dicto_zaap, pause=pause)

def list2dicto_Zaap(listZaap):
    dicto_all_zaap = {'Bord de la foret malefique':0,'Chateau d Amakna':1,'Coin des Bouftous':2,'Montagne des Craqueleurs':3,'Plaine des Scarafeuilles':4,
                      'Port de Madrestam':5,'Village d Amakna':6,'Cite d Astrub':7,'Tainela':8,'Rivage sufokien':9,'Sufokia':10,
                      'Temple des alliances':11,'Bonta Centre-ville':12,'Brakmar Centre-ville':13,'Village cotier':14,'Village de la Canopee':15,
                      'Entree du chateau de Harebourg':16,'La Bourgade':17,'Village enseveli':18,'Laboratoires abandonnes':19,'Ile de la Cawotte':20,
                      'Route des Roulottes':21,'Terres Desacrees':22,'Village des Eleveurs':23,'Faubourgs de Pandala':24,'Champs de Cania':25,
                      'Lac de Cania':26,'Massif de Cania':27,'Plaine des Porkass':28,'Plaines Rocheuses':29,'Routes Rocailleuses':30,'Village des Brigandins':31,
                      'Dunes des ossements':32}

    dicto_zaap_temp = {}
    for i in listZaap:
        dicto_zaap_temp[dicto_all_zaap[i]] = i

    dicto_zaap = {}
    count = 0
    for i in sorted(dicto_zaap_temp):
        dicto_zaap[dicto_zaap_temp[i]] = count
        count = count + 1
    return dicto_zaap




