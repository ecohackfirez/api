from google.appengine.ext.webapp.util import run_wsgi_app
"""API proxy to CartoDB.

"""

import json
import itertools
import logging
import os
import random
import urllib
import webapp2

from collections import defaultdict

from google.appengine.api import memcache
from google.appengine.api import urlfetch

class ApiHandler(webapp2.RequestHandler):
    def get(self):
        """Handler for WebGL requests returning GEOJSON.
        
        /api/webgl?mag=b&count=10

        Example:
          [["2012", [28.915, 19.781, 306.5]], ["2011", [21.864,98.677, 319.8]], ["2010", [11.105, -6.337, 332.8]]]
        """
        mag = self.request.get('mag', 'brightness')
        count = self.request.get_range('count', default=10)
        
        key = 'mag=%s,count=%s' % (mag, count)
        value = memcache.get(key)

        if not value:
            sql = "SELECT lat, lon, %s, date FROM fires limit %s" % (mag, count)
            url = 'http://ecohackfirez.cartodb.com/api/v2/sql?%s' % urllib.urlencode(dict(q=sql))
            content = json.loads(urlfetch.fetch(url, deadline=60).content) # TODO: retry
            if not content.has_key('error'):
                results = map(lambda row: [row['date'], [row['lat'], row['lon'], row[mag]]], content['rows'])
                aggregated = defaultdict(list) # By date              

                for row in results:
                    aggregated[row[0]].append(row[1])

                values = []
                for key in aggregated.keys():
                    values.append(key)
                    values.append(list(itertools.chain(*aggregated[key])))
                value = json.dumps(values)
                memcache.add(key, value)
        
        if not value:
            value = []

        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(value)

application = webapp2.WSGIApplication(
         [('/api/webgl', ApiHandler)],
         debug=True
)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
