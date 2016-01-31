try:
    daten = open('sketch.txt')

    for zeile in daten:
        try:
            (rolle, aussage) = zeile.split(':', 1)
            print(rolle, end='')
            print(' sagte: ', end='')
            print(aussage, end='')
        except ValueError:
            pass

    daten.close()
except IOError:
    print('Datei nicht auffindbar!')

