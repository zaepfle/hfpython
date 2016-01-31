# coding: utf-8

import android
import json
import time

from urllib import urlencode
from urllib2 import urlopen

start_mld     = "Die Laufzeiten-App des DJLV"
listentitel    = 'Hier ist die Liste aller Sportler:'
end_mld      = "Beende die DJLV-App."
webserver    = 'http://192.168.178.21:8080'
namen_cgi = '/cgi-bin/namen_generieren.py'
daten_cgi  = '/cgi-bin/daten_generieren.py'

def server_senden(url, post_daten=None):
    if post_daten:
        seite = urlopen(url, urlencode(post_daten))
    else:
        seite = urlopen(url)
    return(seite.read().decode("utf8"))
app = android.Android()

def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

status_update(start_mld)

alle_sportler = sorted(json.loads(server_senden(webserver + namen_cgi)))
sportlernamen = [sp[0] for sp in alle_sportler]
app.dialogCreateAlert(listentitel)
app.dialogSetSingleChoiceItems(sportlernamen)
app.dialogSetPositiveButtonText('Wählen')
app.dialogSetNegativeButtonText('Beenden')
app.dialogShow()
antw = app.dialogGetResponse().result

if antw['which'] in ('positive'):
    gesuchter_sportler = app.dialogGetSelectedItems().result[0]
    der_sportler = alle_sportler[gesuchter_sportler][1]
    sportler = json.loads(server_senden(webserver + daten_cgi,
                                    {'der_sportler': der_sportler}))

    sportler_title = sportler['Name'] + 's (' + sportler['Geb'] + '), Bestzeiten:'
    app.dialogCreateAlert(sportler_title)
    app.dialogSetItems(sportler['Top3'])
    app.dialogSetPositiveButtonText('OK')
    app.dialogSetNegativeButtonText('Neue Zeit')
    app.dialogShow()

    antw = app.dialogGetResponse().result

    if antw['which'] in ('positive'):
        pass
    elif antw['which'] in ('negative'):
        zeit_titel = 'Neue Zeit eingeben'
        zeit_text = 'Geben Sie einen neue Laufzeit ein ' + sportler['Name'] + ': '
        neue_zeit_cgi = '/cgi-bin/neue_zeit.py'

        antw = app.dialogGetInput(zeit_titel, zeit_text).result
        if antw is not None:
            neue_zeit = antw
            server_senden(webserver + neue_zeit_cgi,
                          {'Zeit': neue_zeit,
                           'Sportler': der_sportler})
status_update(end_mld)




