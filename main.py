import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import util, template
from google.appengine.ext import db
from google.appengine.api import mail
from appengine_utilities import sessions
import datetime


class HomeHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(template.render("Templates/welcome.html")

app = webapp2.WSGIApplication([
  ('/', HomeHandler)], debug=True)