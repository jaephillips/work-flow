from google.appengine.ext import ndb

class FormModel(ndb.Model):
    name = ndb.StringProperty()
    task = ndb.StringProperty()
    level = ndb.StringProperty()
    date = ndb.StringProperty()
    instructions = ndb.StringProperty()
    assignBy = ndb.StringProperty()
    email= ndb.StringProperty()
    