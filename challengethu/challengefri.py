#!usr/bin/env python3

#astro= {"number": 3, "message": "success", "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}]}

import urllib.request
import json

url= "http://api.open-notify.org/astros.json"

fileobject=urllib.request.urlopen(url)
jsontext=fileobject.read()
astro=json.loads(jsontext)
print(f("People in Space: " (astro["number"])+ "\n")
        for x in astro["people"]:
        #!usr/bin/env python3

#astro= {"number": 3, "message": "success", "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}]}

import urllib.request
import json

url= "http://api.open-notify.org/astros.json"

fileobject=urllib.request.urlopen(url)
jsontext=fileobject.read()
astro=json.loads(jsontext)
print(f("People in Space: " (astro["number"])+ "\n")
        for x in astro["people"]:
        print(f"{x["name"]} is on the {x["craft"]})print(f"{x["name"]} is on the {x["craft"]})
