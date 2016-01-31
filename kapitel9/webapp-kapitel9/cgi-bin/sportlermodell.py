import sqlite3

db_name = 'trainerdaten.sqlite'

def namen_lesen():
    verbindung = sqlite3.connect(db_name)
    cursor = verbindung.cursor()
    ergebnis = cursor.execute("""SELECT name FROM sportler_t""")
    antwort = [zeile[0] for zeile in ergebnis.fetchall()]
    verbindung.close()
    return(antwort)

def sportler_zu_id(sportler_id):
    verbindung = sqlite3.connect(db_name)
    cursor = verbindung.cursor()

    ergebnis = cursor.execute("""SELECT name, geb FROM sportler_t WHERE id=?""",
 						(sportler_id,))
    (name, geb) = ergebnis.fetchone()

    ergebnis = cursor.execute("""SELECT zeit FROM zeiten_t WHERE sportler_id=?""",
                                     			(sportler_id,))
    daten = [zeile[0] for zeile in ergebnis.fetchall()]

    antwort = {	'Name':   name, 
              	'Geb':    geb,
               	'Daten':   daten,
               	'Top3':   daten[0:3]}
    verbindung.close()
    return(antwort)

def namen_ids_lesen():
    verbindung = sqlite3.connect(db_name)
    cursor = verbindung.cursor()
    ergebnis = cursor.execute("""SELECT name, id FROM sportler_t""")
    antwort = ergebnis.fetchall()
    verbindung.close()
    return(antwort)
