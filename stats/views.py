import pickle
import sys

from django.http import HttpResponse
from django.shortcuts import render_to_response
from google.appengine.ext import db

from third_party.graphy.backends import google_chart_api

from stats import models


def index(request):
  data = [2, 4, 7, 7, 4, 6, 8, 2, 1, 2, 5, 8, 8]
  chart = google_chart_api.LineChart(data)
  context = {'chart': chart.display.Img(300, 200)}
  return render_to_response('stats/index.html', context)


def add(request, id, key, value):
  c = models.Chart.get_or_create(id)
  data = {}
  if c.data:
    data = pickle.loads(c.data)
  data[key] = value
  c.data = pickle.dumps(data)
  c.put()
  return HttpResponse("data is %r" % data)
