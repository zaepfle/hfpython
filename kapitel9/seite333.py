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
