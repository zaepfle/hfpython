def print_lvl(liste, ebene=0):
    """Diese alle Elemente einer Liste, rekursiv in eingebettete Listen
    absteigend aus (falls erforderlich)."""

    for element in liste:
        if isinstance(element, list):
            print_lvl(element, ebene+1)
        else:
            if einzug:
                for tab in range(ebene):
                    print("\t", end='')
            print(element)