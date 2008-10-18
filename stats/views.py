import pickle

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

from google.appengine.ext import db
from google.appengine.api import users

from stats import models


def index(request):
  return list(request)


def add(request, id, key, value):
  chart = models.Chart.get_or_create(id)
  if chart.secure_key is not None:
    raise Http404
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


def get_secure_key(request, id):
  chart = models.Chart.get_or_create(id)
  if chart.user is None or chart.user == users.get_current_user():
    return HttpResponse(chart.get_secure_key())
  raise Http404


def secure_add(request, secure_key, id, key, value):
  chart = models.Chart.get_or_create(id)
  if chart.secure_key != secure_key:
    raise Http404
  chart.data[int(key)] = float(value)
  chart.put()
  context = {'chart': chart}
  return render_to_response('stats/add.html', context)
