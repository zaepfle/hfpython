daten = open('sketch.txt')

for zeile in daten:
    try:
        (rolle, aussage) = zeile.split(':', 1)
        print(rolle, end='')
        print(' sagte: ', end='')
        print(aussage, end='')
    except:
        pass

daten.close()

