from django.http import HttpResponse
from google.appengine.ext import db
import pickle

class Chart(db.Model):
  id = db.StringProperty(required=True)
  data = db.BlobProperty()


def index(request):
  return HttpResponse("Hello world!")


def add(key, value):
  m = Chart().gql('WHERE key = :key', key=key)
