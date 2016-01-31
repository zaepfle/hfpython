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
    with open('mann_daten.txt', 'w') as mann_datei,
         open('anderer_daten.txt', 'w') as anderer_datei:
        print(mann, file=mann_datei)
        print(anderer, file=anderer_datei)

except IOError:
    print('Dateifehler')
    

 
