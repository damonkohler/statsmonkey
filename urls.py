# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import *

urlpatterns = patterns('stats.views',
  (r'^$', 'index'),
  (r'^add/(\w+)/(\d+)/([0-9.\-]+)/?', 'add'),
  (r'^list/?', 'list'),
  (r'^show/(\w+)/?', 'show'),
  (r'^secure/add/([0-9a-f\-]+)/(\w+)/(\d+)/([0-9.\-]+)/?', 'secure_add'),
  (r'^secure/(\w+)/?', 'get_secure_key'),
)
