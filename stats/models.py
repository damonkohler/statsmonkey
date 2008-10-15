import pickle

from django.http import HttpResponse
from google.appengine.ext import db

class Chart(db.Model):
  id = db.StringProperty(required=True)
  data = db.BlobProperty()

  @classmethod
  def get_by_id(cls, id):
    return cls.gql('WHERE id = :id LIMIT 1', id=id).get()

  @classmethod
  def get_or_create(cls, id):
    c = cls.get_by_id(id)
    if c:
      return c
    return cls(id=id)
