# coding: utf-8

import sqlite3

verbindung = sqlite3.connect('trainerdaten.sqlite')

cursor = verbindung.cursor()
cursor.execute("""CREATE TABLE sportler_t (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    geb DATE NOT NULL )""")
cursor.execute("""CREATE TABLE zeiten_t (
                  sportler_id INTEGER NOT NULL,
                  zeit TEXT NOT NULL,
                  FOREIGN KEY (sportler_id) REFERENCES sportler_t)""")

verbindung.commit()
verbindung.close()
    
