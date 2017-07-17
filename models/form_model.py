from google.appengine.ext import ndb

class FormModel(ndb.Model):
    form_name = ndb.StringProperty()
    form_task = ndb.StringProperty()
    form_level = ndb.StringProperty()
    form_date = ndb.StringProperty()
    form_instructions = ndb.StringProperty()
    user_email= ndb.StringProperty()
    