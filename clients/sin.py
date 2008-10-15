#!/usr/bin/env python
import math
import urllib2
import sys

chart_name = sys.argv[1]


for i in range(100):
  host = 'http://stats-monkey.appspot.com'
  url = '%s/add/%s/%d/%.2f' % (host, chart_name, i, math.sin(i/10.0) * 100)
  print url
  urllib2.urlopen(url)
