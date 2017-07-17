from google.appengine.ext import ndb

class Model(ndb.Model):
	dog_name = ndb.StringProperty()
	pic_url = ndb.StringProperty()
	user_email = ndb.StringProperty()