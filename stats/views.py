import pickle 

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from google.appengine.ext import db

from stats import models


def index(request):
  return list(request)
  #data = [2, 4, 7, 7, 4, 6, 8, 2, 1, 2, 5, 8, 8]
  #chart = google_chart_api.LineChart(data)
  #context = {'chart': chart.display.Img(300, 200)}
  #return render_to_response('stats/index.html', context)


def add(request, id, key, value):
  chart = models.Chart.get_or_create(id)
  chart.data[int(key)] = float(value)
  chart.put()
  context = {'chart': chart}
  return render_to_response('stats/add.html', context)


def list(request):
  charts = models.Chart.get_all()
  context = {'num_charts': len(charts),
             'charts': charts,
            }
  return render_to_response('stats/list.html', context)


def show(request, id):
  chart = models.Chart.get_by_id(id)
  if chart is None:
    raise Http404
  context = {'chart': chart}
  return render_to_response('stats/show.html', context)
