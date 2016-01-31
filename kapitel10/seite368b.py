import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

import geburtDB

class GeburtsinfosForm(djangoforms.ModelForm):
    class Meta:
        model = geburtDB.Geburtsinfos

class IndexSeite(webapp.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'titel': 'Geben Sie Ihre Geburtsinfos an'})
        html = html + template.render('templates/form_anfang.html', {})
        html = html + str(GeburtsinfosForm(auto_id=False))     
        html = html + template.render('templates/form_ende.html', {'untertitel': 'Infos senden'})
        html = html + template.render('templates/footer.html', {'links': ''})   
        self.response.out.write(html)

def main():
    app = webapp.WSGIApplication([('/.*', IndexSeite)], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()