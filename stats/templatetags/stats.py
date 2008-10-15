from django import template

from graphy.backends import google_chart_api

register = template.Library()

@register.filter
def chart_anchor(chart):
  """Get the URL to the "show" page for this chart."""
  return '<a href="%s">%s</a>' % (chart_url(chart), chart.id)

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
  return chart.display.Img(300, 200)
