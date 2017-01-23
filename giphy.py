#!/usr/bin/env python

"""
Copyright (c) 2016 Carson Evans

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

--------------------------------------------------------------------------------

README



"""

import os
import sys
import urllib2
import json

if len(sys.argv) < 2:
	print ("Usage: %s <search terms>" % sys.argv[0])
	exit(1)

API_HOST="http://api.giphy.com"
API_ENDPOINT="/v1/gifs/search"
API_KEY=os.getenv("GIPHY_API_KEY")
RESULT_RATING=os.getenv("GIPHY_RESULT_RATING")

if not API_KEY or not RESULT_RATING:
	print "Required environment variables do not exist."
	print "See https://github.com/carc1n0gen/giphy-tool for example configuration."
	exit(2)

query_string = "?q=%s&rating=%s&api_key=%s" % ("+".join(sys.argv[1:]), RESULT_RATING, API_KEY)
request = urllib2.Request("%s%s%s" % (API_HOST, API_ENDPOINT, query_string))

try:
	f = urllib2.urlopen(request)
	json = json.loads(f.read())
	print json['data'][0]['images']['downsized']['url']
except e:
	print e
