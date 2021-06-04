#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:40:34 2021

@author: Yimin
"""

from selenium import webdriver
import json
import pickle
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import html
from time import sleep
import pandas as pd
import numpy as np
import re
import requests




driver = webdriver.Chrome('/Users/Bg_rice/Downloads/chromedriver')

elems = []
for page_number in range(1,44):
    
    driver.get("https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=phone+case&ltype=wholesale&SortType=default&page={}".format(page_number))
    sleep(2)
    
    
    tree = html.fromstring(driver.page_source)
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))
#    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#    sleep(1)
        
    
    for elem in tree.xpath('//li[@class="list-item"]'):
        title = elem.xpath('.//a[@class="item-title"]/@title')
        price = elem.xpath('.//span[@class="price-current"]/text()')
        rating = elem.xpath('.//span[@class="rating-value"]/text()')
        number_sold = elem.xpath('.//a[@class="sale-value-link"]/text()')
        if_is_free_shipping = elem.xpath('.//span[@class="shipping-value"]/text()')
        store = elem.xpath('.//a[@class="store-name"]/text()')
#        print(title,price,rating,number_sold,if_is_shipping,store)
        
        elem = {
            'title': title,
            'price': price,
            'rating': rating,
            'number_sold': number_sold,
            'if_is_free_shipping': if_is_free_shipping,
            'store': store
        
        }
        elems.append(elem.copy())

    
df = pd.DataFrame(elems)
#df.to_csv("aliexpress.csv", index=False)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    