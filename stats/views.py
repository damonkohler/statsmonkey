from django.http import HttpResponse
from google.appengine.ext import db
import pickle

from stats import models


def index(request):
  return HttpResponse("Hello world!")


def add(key, value):
  m = models.Chart().gql('WHERE key = :key', key=key)
