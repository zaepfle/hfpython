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
    mann_datei = open('mann_datei.txt', 'w')
    anderer_datei = open('anderer_datei.txt', 'w')
    print(mann, file=mann_datei)
    print(anderer, file=anderer_datei)
except IOError:
    print('Fehler beim Speichern in Dateien!')
finally:
    mann_datei.close()
    anderer_datei.close
