# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:24:26 2020

@author: Acer
"""
import pandas as pd
from selenium import webdriver

##Open the df##
read_names=pd.read_csv('names.csv')

def player(toPlay):
    gaana_url="https://gaana.com/search/"+toPlay
    driver=webdriver.Chrome('chromedriver.exe')
    driver.get(gaana_url)
    button=driver.find_element_by_class_name('img')
    button.click()
    
        
songToBePlayed=read_names['Names'].sample(axis=0).values[0]

#Play the Song#
player(songToBePlayed)