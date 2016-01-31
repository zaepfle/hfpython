import pickle

mann = []
anderer = []

try:
    daten = open('sketch.txt')

    for zeile in daten:
        try:
            (rolle, aussage) = zeile.split(':', 1)
            aussage = aussage.strip()
            if rolle == 'Man':
                mann.append(aussage)
            elif rolle == 'Other Man':
                anderer.append(aussage)
        except ValueError:
            pass

    daten.close()
except IOError:
    print('Datei nicht auffindbar!')

try:
    with open('mann_daten.txt', 'wb') as mann_datei, \
         open('anderer_daten.txt', 'wb') as anderer_datei:
        pickle.dump(mann, mann_datei)
        pickle.dump(anderer, anderer_datei)

except IOError as ioerr:
    print('Dateifehler: ' + str(ioerr))

except PickleError as perr:
    print('Pickle-Fehler: ' + str(perr))
    
    

