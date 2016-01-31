daten = open('sketch.txt')

for zeile in daten:
    (rolle, aussage) = zeile.split(':', 1)
    print(rolle, end='')
    print(' sagte: ', end='')
    print(aussage, end='')

daten.close()

