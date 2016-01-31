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

verbindung.close()
