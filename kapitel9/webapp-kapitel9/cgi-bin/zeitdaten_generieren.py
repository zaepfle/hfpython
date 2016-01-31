#! /usr/local/bin/python3

import cgi
import sportlermodell
import yate

form_daten = cgi.FieldStorage()
sportler_id = form_daten['sportlerwahl'].value
sportler = sportlermodell.sportler_zu_id(sportler_id)

print(yate.antwort_anfang())
print(yate.seitenanfang("Die DJLV-Laufzeiten"))    
print(yate.heading("Sportler: " + sportler['Name'] +
                   ", Geb.: " + sportler['Geb']))
print(yate.para("Die Bestzeiten für diesen Sportler sind:"))
print(yate.u_liste(sportler['Top3']))
print(yate.para("Alle Laufzeiten: " + str(sportler['Daten']) + 
			" (doppelte Zeiten entfernt)."))
print(yate.seitenende({"Home": "/index.html",
                        "Anderen Sportler auswählen": "liste_generieren.py"}))
