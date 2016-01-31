
from google.appengine.ext import db

class Geburtsinfos(db.Model):
    name =          db.StringProperty()
    geburtsdatum = db.DateProperty()
    geburtszeit = db.TimeProperty()

