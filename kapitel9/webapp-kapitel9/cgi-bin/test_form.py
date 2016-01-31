#! /usr/local/bin/python3
# coding: utf-8

import yate

print(yate.antwort_anfang('text/html'))
print(yate.form_erstellen('neue_zeit.py', ['zeitwert'], text='Senden'))
