daten = open('sketch.txt')

for zeile in daten:
    (rolle, aussage) = zeile.split(':')
    print(rolle, end='')
    print(' sagte: ', end='')
    print(aussage, end='')
