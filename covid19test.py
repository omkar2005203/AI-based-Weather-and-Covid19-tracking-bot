# importing libraries 

import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
import json
import re
import globalConfigs as c

 # define desired replacements here

# use these three lines to do the replacement

#Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions


def covidshow():
    
    data=c.response.json()

    op = json.dumps(data,indent=4) # string op

    rep = {"{": "", "}": ""}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))],op)

    return text


def infectsum():
    data=c.response.json()
    sum=0
    for v in data:
         sum = sum + data[v]
         
    return sum

    











# print(covidshow())

# print(infectsum())

