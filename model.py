import datetime
import json

from google.appengine.ext import ndb


class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class Action(ndb.Model):
    date = ndb.DateTimeProperty(required=True, auto_now_add=True)
    problem = ndb.StringProperty(required=True)
    type_ = ndb.StringProperty(required=True)
    result = ndb.JsonProperty(required=True)


def create_action(type_, key, data):
    action_obj = Action(problem=key, type_=type_, result=data)
    action_obj.put()

def get_actions():
    actions = [x.to_dict() for x in Action.query().order(Action.date).fetch()]
    return json.dumps(actions, cls=MyJsonEncoder)
