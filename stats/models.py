import pickle

from django.http import HttpResponse
from google.appengine.ext import db

class Chart(db.Model):
  # TODO: rename id to name
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

  @classmethod
  def get_all(cls):
    return cls.all().fetch(1000)
