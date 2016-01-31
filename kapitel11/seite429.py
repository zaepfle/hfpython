# coding: utf-8

import time
import android

from such_es import such_besten
from zeit2seks2zeit import zeit2seks, seks2zeit, zeit_formatieren

def zeit_suchen(suchwert, zielliste):
    was = zeit2seks(suchwert)
    wo = [zeit2seks(t) for t in zielliste]
    antw = such_besten(was, wo)
    return(seks2zeit(antw))

def status_update(mld, wie_lang=2):
    app.makeToast(mld)
    time.sleep(wie_lang)

def dialog_an(titel, daten, funk, pos='Wählen', neg='Ende'):
    app.dialogCreateAlert(titel)
    funk(daten)
    app.dialogSetPositiveButtonText(pos)
    if neg:
        app.dialogSetNegativeButtonText(neg)
    app.dialogShow()
    return(app.dialogGetResponse().result)

strecken = [ '2mi', '5km', '5mi', '10km', '15km', '10mi', '20km',
             'Halb-Marathon', '25km', '30km', 'Marathon' ]
start_mld = "Willkommen bei der Marathon-App"
end_mld = "Beende die Marathon-App."

zeilendaten = {}
with open('/sdcard/sl4a/scripts/Laufzeiten.csv') as zeiten:
    spalten = zeiten.readline().strip().split(',')
    spalten.pop(0)    
    for daten in zeiten:
        zeile = daten.strip().split(',')
        zeile_label = zeile.pop(0)
        inneres_dict = {}
        for i in range(len(spalten)):
            inneres_dict[zeit_formatieren(zeile[i])] = spalten[i]
        zeilendaten[zeile_label] = inneres_dict

app = android.Android()
status_update(start_mld)
antw = dialog_an("Wählen Sie eine Strecke", strecken, app.dialogSetSingleChoiceItems)
if antw['which'] in ('positive'):
    laufstrecke = app.dialogGetSelectedItems().result[0]
    laufstrecke = strecken[laufstrecke]
    laufzeit = app.dialogGetInput("Ihre Zeit für " + laufstrecke + " war:",
                                           "Nutzen Sie das HH:MM:SS-Format:").result
    zeit_in_tab = zeit_suchen(zeit_formatieren(laufzeit), zeilendaten[laufstrecke])
    tab_spaltenkopf = zeilendaten[laufstrecke][zeit_in_tab]
    antw = dialog_an("Strecke für die Vorhersage?", strecken, app.dialogSetSingleChoiceItems)
    if antw['which'] in ('positive'):
        vorhersagestrecke = app.dialogGetSelectedItems().result[0]
        vorhersagestrecke = strecken[vorhersagestrecke]
        vorhersage = [k for k in zeilendaten[vorhersagestrecke].keys()
                          if zeilendaten[vorhersagestrecke][k] == tab_spaltenkopf]
        dialog_an('Die geschätzte Laufzeit für ' + vorhersagestrecke + ' ist: ',
                             vorhersage, app.dialogSetItems, "OK", None)
status_update(end_mld)
