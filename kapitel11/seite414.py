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
