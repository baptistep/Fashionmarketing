import webapp2
import os
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(template.render('templates/welcome.html', locals()))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()