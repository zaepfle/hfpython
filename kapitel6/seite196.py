def säubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)

class Sportler:
    def __init__(self, ein_name, ein_geb=None, ein_zeiten=[]):
        self.name = ein_name
        self.geb = ein_geb
        self.zeiten = ein_zeiten
        
    def top3(self):
        return(sorted(set([säubern(t) for t in self.zeiten]))[0:3])

def datei_lesen(dateiname):
    try:
        with open(dateiname) as f:
            daten = f.readline()
        templ = daten.strip().split(',')
        return(Sportler(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('Dateifehler: ' + str(ioerr))
        return(None)
    
ron = datei_lesen('ron2.txt')
sarah = datei_lesen('sarah2.txt')
mark = datei_lesen('mark2.txt')
julie = datei_lesen('julie2.txt')

print(ron.name + "s Bestzeiten sind: " + str(ron.top3()))
print(sarah.name + "s Bestzeiten sind: " + str(sarah.top3()))
print(mark.name + "s Bestzeiten sind: " + str(mark.top3()))
print(julie.name + "s Bestzeiten sind: " + str(julie.top3()))
