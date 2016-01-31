from such_es import such_besten
from zeit2seks2zeit import zeit2seks, seks2zeit

def zeit_suchen(suchwert, zielliste):
    was = zeit2seks(suchwert)
    wo = [zeit2seks(t) for t in zielliste]
    antw = such_besten(was, wo)
    return(seks2zeit(antw))

zeilendaten = {}

with open('Laufzeiten.csv') as zeiten:
    spalten = zeiten.readline().strip().split(',')
    spalten.pop(0)
    
    for daten in zeiten:
        zeile = daten.strip().split(',')
        zeile_label = zeile.pop(0)
        inneres_dict = {}
        for i in range(len(spalten)):
            inneres_dict[zeile[i]] = spalten[i]
        zeilendaten[zeile_label] = inneres_dict

laufzeit = input('Gelaufene Zeit: ')
laufstrecke = input('Gelaufene Strecke: ')
vorhersage_strecke = input('Strecke für die Vorhersage: ')

bester_treffer = zeit_suchen(laufzeit, zeilendaten[laufstrecke])
beste_spalte = zeilendaten[laufstrecke][bester_treffer]

vorhersage = [k for k in zeilendaten[vorhersage_strecke].keys()
                  if zeilendaten[vorhersage_strecke][k] == beste_spalte]

print('Die geschätzte Laufzeit für ' + vorhersage_strecke + ' ist: ' + vorhersage[0] + '.')
