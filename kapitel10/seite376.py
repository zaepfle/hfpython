# coding: utf-8

from google.appengine.ext import db

_FLOSSEN = ['Sichel', 'Dreieck', 'Gerundet']
_WALE    = ['Buckel', 'Orca', 'Blau', 'Killer', 'Beluga', 'Fin', 'Grau', 'Pott']
_BLASE   =  ['Hoch', 'Buschig', 'Dicht']
_WELLEN  =  ['Flach', 'Klein', 'Mittel', 'Breit', 'Brechend', 'Hoch']

class Sichtung(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()     
    datum = db.DateProperty()      
    zeit = db.TimeProperty()      
    ort =   db.StringProperty(multiline=True)
    flossentyp =   db.StringProperty(choices=_FLOSSEN)
    walart = db.StringProperty(choices=_WALE)
    blastyp =  db.StringProperty(choices=_BLASE)
    wellentyp =  db.StringProperty(choices=_WELLEN)

