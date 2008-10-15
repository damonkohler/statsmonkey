from django.http import HttpResponse
from google.appengine.ext import db
import pickle

class Chart(db.Model):
  id = db.StringProperty(required=True)
  data = db.BlobProperty()

  @classmethod
  def get_by_id(cls, id):
    return cls.gql('WHERE id = :id', id=id)
