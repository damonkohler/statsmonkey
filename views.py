from django.http import HttpResponse
from google.appengine.ext import db
import pickle

class Chart(db.Model):
  key = db.StringProperty(required=True)
  data = db.BlogProperty()


def index(request):
  return HttpResponse("Hello world!")


def add(key, value):
  m = Chart().gql('WHERE key = :key', key=key)
