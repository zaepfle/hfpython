# coding: utf-8

import android
from urllib import urlencode
from urllib2 import urlopen

server_titel  = 'Welchen Server soll ich nutzen?'
server_text    = "Bitte bestätigen Sie den für die Laufzeit Ihres Sportlers zu nutzenden Server:"
zeit_titel  = 'Dateneingabe'
zeit_text    = 'Geben Sie einen neue Laufzeit ein:'
webserver    = 'http://192.168.1.33:8080'
neue_zeit_cgi  = '/cgi-bin/neue_zeit.py'

app = android.Android()

def server_senden(url, post_daten=None):
    if post_daten:
        seite = urlopen(url, urlencode(post_daten))
    else:
        seite = urlopen(url)
    return(seite.read().decode("utf8"))

antw = app.dialogGetInput(server_titel, server_text, webserver).result

if antw is not None:
    webserver = antw
    antw = app.dialogGetInput(zeit_titel, zeit_text).result
    if antw is not None:
        neue_zeit = antw
        server_senden(webserver + neue_zeit_cgi, {'zeitwert': neue_zeit})
