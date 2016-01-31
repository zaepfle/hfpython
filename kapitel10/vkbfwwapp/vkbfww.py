# coding: utf-8  

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from google.appengine.api import users

import vkbfwwDB

class SichtungForm(djangoforms.ModelForm):
    class Meta:
        model = vkbfwwDB.Sichtung
        exclude = ['benutzer']

class SichtungEingabeSeite(webapp.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'titel': 'Mögliche Sichtung melden'})
        html = html + template.render('templates/form_anfang.html', {})
        html = html + str(SichtungForm())
        html = html + template.render('templates/form_ende.html', {'untertitel': 'Sichtung senden'})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

    def post(self):
        sichtung = vkbfwwDB.Sichtung()
        sichtung.name = self.request.get('name')
        sichtung.email = self.request.get('email')
        sichtung.datum = self.request.get('datum')
        sichtung.zeit = self.request.get('zeit')
        sichtung.ort = self.request.get('ort')
        sichtung.flossentyp = self.request.get('flossentyp')
        sichtung.walart = self.request.get('walart')
        sichtung.blastyp =self.request.get('blastyp')
        sichtung.wellentyp = self.request.get('wellentyp')
        sichtung.benutzer = users.get_current_user()
   
        sichtung.put()

        html = template.render('templates/header.html', 
					{'titel': 'Danke!'})
        html = html + "<p>Danke für die Sichtungsdaten.</p>"
        html = html + template.render('templates/footer.html',
                    {'links': '<a href=”/”>Weitere Sichtung</a> melden.'})

        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', SichtungEingabeSeite)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
