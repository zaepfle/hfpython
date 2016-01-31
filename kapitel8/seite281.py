#! /usr/local/bin/python3
# coding: utf-8

import cgi
import json
import sportlermodell
import yate

alle_sportler = sportlermodell.konserve_lesen()
form_data = cgi.FieldStorage()
sportlername = form_data['der_sportler'].value
print(yate.antwort_anfang('application/json'))
print(json.dumps(alle_sportler[sportlername]))
