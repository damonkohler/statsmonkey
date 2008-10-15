from django.http import HttpResponse
from django.shortcuts import render_to_response
from google.appengine.ext import db
import pickle

from stats import models


def index(request):
  return render_to_response('stats/index.html', {})


def add(key, value):
  m = models.Chart.get_by_id(key)
