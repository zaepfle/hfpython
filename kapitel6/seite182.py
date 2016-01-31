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
    
sarah = datei_lesen('sarah2.txt')

sarah_daten = {}
sarah_daten['Name'] = sarah.pop(0)
sarah_daten['Geb'] = sarah.pop(0)
sarah_daten['Zeiten'] = sarah

print(sarah_daten['Name'] + "s Bestzeiten sind: " +
        str(sorted(set([säubern(t) for t in sarah_daten['Zeiten']]))[0:3]))
