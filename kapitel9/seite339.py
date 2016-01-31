#! /usr/local/bin/python3

import sportlermodell
import yate

alle_sportler = sportlermodell.namen_ids_lesen()

print(yate.antwort_anfang())
print(yate.seitenanfang("Die Sportler des DJLV"))
print(yate.form_anfang("zeitdaten_generieren.py"))
print(yate.para("Wählen Sie einen Sportler aus der Liste aus:"))

for sportler in sorted(alle_sportler):
    print(yate.radio_button_id("sportlerwahl", sportler[0], sportler[1]))
print(yate.form_ende("Auswählen"))
print(yate.seitenende({"Home": "/index.html"}))
