import pickle
import uuid

from django.http import HttpResponse
from google.appengine.ext import db


class Chart(db.Model):
  # TODO: rename id to name
  id = db.StringProperty(required=True)
  _pickled_data = db.BlobProperty()
  data = {}
  secure_key = db.StringProperty()
  user = db.UserProperty()

  def put(self):
    self._pickle()
    super(Chart, self).put()

  def _pickle(self):
    self._pickled_data = pickle.dumps(self.data)

  def _unpickle(self):
    self.data = pickle.loads(self._pickled_data)

  @classmethod
  def get_by_id(cls, id):
    chart = cls.gql('WHERE id = :id LIMIT 1', id=id).get()
    if chart is not None:
      chart._unpickle()
    return chart

  @classmethod
  def get_or_create(cls, id):
    chart = cls.get_by_id(id)
    if chart:
      return chart
    return cls(id=id)

  @classmethod
  def get_all(cls):
    charts = cls.all().fetch(1000)
    for chart in charts:
      chart._unpickle()
    return charts

  def get_secure_key(self):
    if self.secure_key is None:
      self.secure_key = str(uuid.uuid4())
      self.user = users.get_current_user()
    self.put()
    return self.secure_key
