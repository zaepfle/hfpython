#! /usr/local/bin/python3

import cgi
import json
import sportlermodell
import yate

alle_sportler = sportlermodell.konserve_lesen()
form_daten = cgi.FieldStorage()
sportlername = form_daten['der_sportler'].value
print(yate.antwort_anfang('application/json'))
print(json.dumps(alle_sportler[sportlername].als_dict))
