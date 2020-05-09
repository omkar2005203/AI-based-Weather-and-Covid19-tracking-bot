import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
import json
import re



# import pyowm
# import globalConfigs as c
# owm = pyowm.OWM(c.api)

# observation = owm.weather_at_place('pune')
# weather = observation.get_weather()
# wind = weather.get_wind()['speed']
# humidity= weather.get_humidity()
# print(weather)
# temperature = weather.get_temperature('celsius')['temp']

# status = weather.get_detailed_status()

# print('wind speed:',(wind)*(18/5))
# print('Temperature',temperature)
# print('Humidity is :',humidity)
# print(status)





##################################################################

def Convert(a): 
    it = iter(a) 
    res_dct = dict(zip(it, it)) 
    return res_dct 


def new():
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
    URL = 'https://www.mohfw.gov.in/'
    SHORT_HEADERS = ['S.No.','State/UT', 
				'Total Confirmed cases','Cured/Discharged/Migrated','Death'] 
    response = requests.get(URL).content 
    soup = BeautifulSoup(response, 'html.parser') 
    header = extract_contents(soup.tr.find_all('th')) 
    stats = [] 
    all_rows = soup.find_all('tr') 
    
    stats.append(SHORT_HEADERS)

    for row in all_rows:
        #print(row) 
        stat = extract_contents(row.find_all('td')) 
        #print(len(stat))
        # print(stat)
        # print(len(stat))
        
        if stat: 
            
            if len(stat) == 5: 
                stat = [*stat] 
                stats.append(stat) 
            elif len(stat) == 5: 
                stats.append(stat) 
            elif len(stat) == 4: 
                stats.append(stat) 
            elif len(stat) == 1: 
                stats.append(stat) 
                
    stats.remove(stats[-1]) 

    q=Convert(stats)

    final_dictionary = json.loads(q) 

    print(q)

    objects = [] 

    for row in stats : 
        objects.append(row[1])  
  
    y_pos = np.arange(len(objects)) 
  
    performance = [] 
    for row in stats : 
        performance.append(int(row[2]) + int(row[3]))
  
    table = tabulate(stats, headers=SHORT_HEADERS) 

    
    #print(stats)
   



print(new())