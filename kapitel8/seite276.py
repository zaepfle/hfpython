# coding: utf-8

import android
import json
import time

from urllib import urlencode
from urllib2 import urlopen

start_mld     = "Trainer Tims Bestzeit-App"
listentitel    = 'Hier ist die Liste aller Sportler:'
end_mld      = "Beende Trainer Tims App."
webserver    = 'http://192.168.1.33:8080'
namen_cgi = '/cgi-bin/namen_generieren.py'

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

sportlernamen = sorted(json.loads(server_senden(webserver + namen_cgi)))
app.dialogCreateAlert(listentitel)
app.dialogSetSingleChoiceItems(sportlernamen)
app.dialogSetPositiveButtonText('Wählen')
app.dialogSetNegativeButtonText('Beenden')
app.dialogShow()
antw = app.dialogGetResponse().result

status_update(end_mld)




