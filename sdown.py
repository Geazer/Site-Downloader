#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import os.path

#It works only with http:// or https://
url = input("Please, enter the site address:")
html = urllib.request.urlopen(url).read()

save_path = input("To save the file?:")

completeName = os.path.join(save_path, "index.html")
f = open(completeName, 'wb')
f.write(html)
