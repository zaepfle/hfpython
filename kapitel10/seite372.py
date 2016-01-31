# coding: utf-8  

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

import vkbfwwDB

class SichtungForm(djangoforms.ModelForm):
    class Meta:
        model = vkbfwwDB.Sichtung

class SichtungEingabeSeite(webapp.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'titel': 'Mögliche Sichtung melden'})
        html = html + template.render('templates/form_anfang.html', {})
        html = html + str(SichtungForm())
        html = html + template.render('templates/form_ende.html', {'untertitel': 'Sichtung senden'})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', SichtungEingabeSeite)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
