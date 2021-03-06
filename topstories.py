#!/usr/bin/python
import requests
from datetime import date
from pprint import pprint
import os,pickle

# SPECIFY YOUR API KEY AS api_key:
# api_key = "yourkeyhere"
from secret import topstories as api_key

"""
Get the urls for the top stories of the day from NYT. Needs an API key from NYT
"""


API_ROOT = "http://api.nytimes.com/svc/topstories/v1/"
#sections = ["home","world","national","politics","nyregion","business","opinion","technology","science","health","sports","arts","fashion","dining","travel","magazine","realestate"]
section = "world"
response_format = "json"
URL = API_ROOT + section + "." + response_format + "?api-key=" + api_key

# API CALL
r = requests.get(URL)
results = r.json()
results = results["results"]


# ------------------------------------------------------------------------------

base_directory = "news/"
if not os.path.exists(base_directory):
    os.mkdir(base_directory)
directory = base_directory + str(date.today())
if not os.path.exists(directory):
    os.mkdir(directory)

    
pickle.dump(results, open(directory+"/results.p", "w"))

