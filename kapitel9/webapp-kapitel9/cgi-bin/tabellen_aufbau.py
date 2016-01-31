# coding: utf-8

import sqlite3

verbindung = sqlite3.connect('trainerdaten.sqlite')
cursor = verbindung.cursor()

import glob
import sportlermodell
datendateien = glob.glob("../daten/*.txt")
alle_sportler = sportlermodell.konserve_machen(datendateien)

for sportler in alle_sportler:

    name = alle_sportler[sportler].name
    geb = alle_sportler[sportler].geb
    cursor.execute("INSERT INTO sportler_t (name, geb) VALUES (?, ?)", (name, geb))
    verbindung.commit()

    cursor.execute("SELECT id from sportler_t WHERE name=? AND geb=?", 
			(name, geb))
    akt_id = cursor.fetchone()[0]
    for zeit in alle_sportler[sportler].saubere_daten:
        cursor.execute("INSERT INTO zeiten_t (sportler_id, zeit) VALUES (?, ?)", 
			(akt_id, zeit))
    verbindung.commit()

verbindung.close()
