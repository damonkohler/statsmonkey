#!/usr/bin/env python
import math
import urllib2

for i in range(100):
  url = 'http://localhost:8082/add/sin/%d/%.2f' % (i, math.sin(i/10.0) * 100)
  print url
  urllib2.urlopen(url)
