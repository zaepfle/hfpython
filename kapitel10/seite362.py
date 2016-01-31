from google.appengine.ext import db

class Sichtung(db.Model):
    name = db.StringProperty()      
    email = db.StringProperty()     
    datum = db.DateProperty()      
    zeit = db.TimeProperty()      
    ort = db.StringProperty()  
    flossentyp = db.StringProperty()  
    walart = db.StringProperty()
    blastyp = db.StringProperty() 
    wellentyp = db.StringProperty() 

