import base64
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexPage(webapp.RequestHandler):
    def get(self):
        template_values = { }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class ShowPage(webapp.RequestHandler):
    def get(self):
        m = base64.decodestring(self.request.get("m"));
        (picker, pickee) = m.split("\n");
        template_values = {
            'picker': picker,
            'pickee': pickee
        }
        path = os.path.join(os.path.dirname(__file__), 'show.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([ ('/', IndexPage),
                                       ('/show', ShowPage)
                                     ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
