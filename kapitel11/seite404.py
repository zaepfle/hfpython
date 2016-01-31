zeilendaten = {}

with open('Laufzeiten.csv') as zeiten:
    spalten = zeiten.readline().strip().split(',')
    spalten.pop(0) 

for daten in zeiten:        
    zeile = daten.strip().split(',')
    zeile_label = zeile.pop(0)  
    zeilendaten[zeile_label] = zeile

anz_spalten = len(spalten)
print(anz_spalten, end=' -> ')
print(spalten)

anz_2mi = len(zeilendaten['2mi'])
print(anz_2mi, end=' -> ')
print(zeilendaten['2mi'])

anz_marathon = len(zeilendaten['Marathon'])
print(anz_marathon, end=' -> ')
print(zeilendaten['Marathon'])
