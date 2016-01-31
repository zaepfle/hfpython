"""Dies ist das Modul “schachtler.py". Es stellt eine Funktion namens
   print_lvl(), die eine Liste mit beliebig vielen eingebetten Listen ausgibt."""

import sys

def print_lvl(liste, einzug=False, ebene=0, dat=sys.stdout):
    """Diese Funktion erwartet ein positionelles Argument namens "liste", das
       eine beliebige Python-Liste (mit eventuellen eingebetten Listen) ist.
       Jedes Element der Liste wird (rekursiv) auf dem Bildschirm auf einer
       eigenen Zeile ausgegeben. Mit dem optionalen zweiten Argument "einzug"
       kann angegeben werden, ob eingebette Listen mit Tabulatoren eingerückt
       werden sollen. Der Standardwert ist false, aktivieren Sie Einrückungen
       mit true. Mit dem optionalen dritten Argument "ebene" (Standardwert 0)
       kann die Einrückungstiefe der ersten Ebene angepasst werden."""

    for element in liste:
        if isinstance(element, list):
            print_lvl(element, einzug, ebene+1, dat)
        else:
            if einzug:
                for tab in range(ebene):
                    print("\t", end='', file=dat)
            print(element, file=dat)
