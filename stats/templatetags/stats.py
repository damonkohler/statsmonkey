from django import template

from third_party.graphy.backends import google_chart_api

register = template.Library()

@register.filter
def chart_url(chart):
  """Get the URL to the "show" page for this chart."""
  return '/show/%s' % chart.id

@register.filter
def image(chart):
  """Get an image tag for this chart."""
  values = []
  keys = chart.data.keys()
  keys.sort()
  for key in keys:
    value = float(chart.data[key])
    values.append(value)
  chart = google_chart_api.LineChart(values)
  return chart.display.Img(200, 300)
