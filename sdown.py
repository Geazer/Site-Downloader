#!/usr/bin/env python3

import urllib.request
#worked only with http:// or https://
url = input("Please, enter the site address:")
html = urllib.request.urlopen(url).read()

f = open('index.html', 'wb')
f.write(html)
