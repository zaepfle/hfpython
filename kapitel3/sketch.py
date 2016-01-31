import os

#os.chdir('/Users/kaiwork/Documents/python/hfpython_code/kapitel3')

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
##            print(rolle, end='')
##            print(' sagte: ', end='')
##            print(aussage, end='')
        except ValueError:
            pass

    daten.close()
except IOError:
    print('Datei nicht auffindbar!')

try:
    with open('mann_datei.txt', 'w') as mann_datei:
        print(mann, file=mann_datei)
    with open('anderer_datei.txt', 'w') as anderer_datei:
        print(anderer, file=anderer_datei)
except IOError as err:
    print('Dateifehler: ' + str(err))
