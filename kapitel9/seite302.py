#! /usr/local/bin/python3

import cgi
import os
import time
import sys
import yate

print(yate.antwort_anfang('text/plain'))
adr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
methode = os.environ['REQUEST_METHOD']
akt_zeit = time.asctime(time.localtime())
print(host + ", " + adr + ", " + akt_zeit + ": " + methode + ": ", 
		end='', file=sys.stderr)
form = cgi.FieldStorage()
for form_element in form.keys():
    print(form_element + '->' + form[form_element].value,
          end=' ',file=sys.stderr)    
print(file=sys.stderr)
print('OK.')
