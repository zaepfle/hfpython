import sqlite3

db_name = 'trainerdaten.sqlite'

def namen_lesen():
    verbindung = sqlite3.connect(db_name)
    cursor = verbindung.cursor()
    ergebnis = cursor.execute("""SELECT name FROM sportler_t""")
    antwort = [zeile[0] for zeile in ergebnis.fetchall()]
    verbindung.close()
    return(antwort)
