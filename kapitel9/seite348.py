#! /usr/local/bin/python3

import cgi
import sqlite3

import yate

print(yate.antwort_anfang('text/plain'))

form_daten = cgi.FieldStorage()
die_id = form_daten['Sportler'].value
die_zeit = form_daten['Zeit'].value

verbindung = sqlite3.connect('trainerdaten.sqlite')
cursor = verbindung.cursor()
cursor.execute("INSERT INTO zeiten_t (sportler_id, zeit) VALUES (?, ?)",
                       (die_id, die_zeit))
verbindung.commit()
verbindung.close()

print('OK.')
