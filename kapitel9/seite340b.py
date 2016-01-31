#! /usr/local/bin/python3

import cgi
import json
import sportlermodell
import yate

form_daten = cgi.FieldStorage()
sportler_id = form_daten['der_sportler'].value
sportler = sportlermodell.sportler_zu_id(sportler_id)
print(yate.antwort_anfang('application/json'))
print(json.dumps(sportler))
