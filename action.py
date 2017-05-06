import json

import webapp2
from google.appengine.api import users
import model


DEBUG = False


class Action(webapp2.RequestHandler):

    def post(self):
        action_type = self.request.path[len('/api/action/'):]
        request = json.loads(self.request.body)
        model.create_action(action_type, self.request.remote_addr, request)

    def get(self):
        if self.request.get('key') == "bananinha":
            self.response.headers['Content-Type'] = 'application/json'
            self.response.write(model.get_actions())
        else:
            self.response.set_status(401)


app = webapp2.WSGIApplication([
    ('/api/action/.*', Action),
], debug=DEBUG)
