# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:34:22 2020

@author: Acer
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
get_names="http://mywordsnthoughts.com/myworld/bollywood/salman-khan-top-100-chartbuster-bollywood-songs-of-his-career/"
request=requests.get(get_names, headers=headers).text
soup=BeautifulSoup(request, 'html.parser')
songNames=[]


##Now scavenge the page for his song names
resultSet=soup.findAll('em')
for result in resultSet:
    wholeTitle=result.text
    filter1=''.join([i for i in wholeTitle if not i.isdigit()])
    filter2=re.sub('\W+', ' ', filter1)
    songNames.append(filter2)

##Let's just save the list for future reference
songdf=pd.DataFrame(songNames, columns=['Names'])
songdf.to_csv('names.csv', index=False)
