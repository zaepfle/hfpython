def säubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)

def datei_lesen(dateiname): 
    try:
        with open(dateiname) as d:
            daten = d.readline()
            return(daten.strip().split(','))
    except IOError as ioerr:
        print('Dateifehler: ' + str(ioerr))
        return(None)
    
ron = datei_lesen('ron.txt')
julie = datei_lesen('julie.txt')
mark = datei_lesen('mark.txt')
sarah = datei_lesen('sarah.txt')

print(sorted(set([säubern(t) for t in ron]))[0:3])
print(sorted(set([säubern(t) for t in julie]))[0:3])
print(sorted(set([säubern(t) for t in mark]))[0:3])
print(sorted(set([säubern(t) for t in sarah]))[0:3])
