def namen_ids_lesen():
    verbindung = sqlite3.connect(db_name)
    cursor = verbindung.cursor()
    ergebnis = cursor.execute("""SELECT name, id FROM sportler_t""")
    antwort = ergebnis.fetchall()
    verbindung.close()
    return(antwort)
