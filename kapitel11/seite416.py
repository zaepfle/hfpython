def such_besten(zu_suchen, suchdaten):

    def abstand_berechnen(eins, zwei):
        if eins == zwei:
            return(0)
        elif eins > zwei:
            return(eins - zwei)
        else:
            return(zwei - eins)

    max_abstand = 9999999
    for elem in suchdaten:
        abstand = abstand_berechnen(elem, zu_suchen)
        if abstand == 0:
            gefunden = elem
            break
        elif abstand < max_abstand:
            max_abstand = abstand
            gefunden = elem
    return(gefunden)
