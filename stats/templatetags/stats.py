from django import template

register = template.Library()

@register.filter
def chart_url(chart):
  return '/show/%s' % chart.id
