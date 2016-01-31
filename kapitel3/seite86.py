daten = open('sketch.txt')

for zeile in daten:
    if not zeile.find(':') == -1:
        (rolle, aussage) = zeile.split(':', 1)
        print(rolle, end='')
        print(' sagte: ', end='')
        print(aussage, end='')

daten.close()

