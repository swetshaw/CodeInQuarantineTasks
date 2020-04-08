# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:31:08 2020

@author: Sweta Shaw
"""
import requests
from bs4 import BeautifulSoup

print("***** Opening the city file *****")
f = open("city.txt",'r')

print("***** Reading the city names *****")
city_list = f.read().splitlines()

city_data_list = []

for city in city_list:
    print("***** Fetching the weather website *****")
    URL = 'https://www.wunderground.com/weather/in/' + city
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('span', class_ = 'wu-value wu-value-to')
    
    print("##### Results are here #####")
    temperature = results[0].text + "F"
    humidity = results[11].text + "%"
    city_data = city + " " + temperature + " " + humidity
    
    city_data_list.append(city_data)

#writing the results into the output.txt file
with open('output.txt', 'w') as f:
    for item in city_data_list:
        f.write("%s\n" % item)