#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:47:47 2021

@author: Yimin
"""


import pandas as pd
import numpy as np

df = pd.read_csv("aliexpress.csv")
df.title.str.split(expand=True).stack().value_counts() 
df['title'] = df['title'].astype(str)
df['title'] = df['title'].str.replace("[",'')
df['title'] = df['title'].str.replace("]",'')
df['title'] = df['title'].str.replace("'",'')
df['title'] = df['title'].astype(str)
df['price'] = df['price'].str.extract(r'(\d+.\d+)').astype('float')
df['rating'] = df['rating'].str.extract(r'(\d+.\d+)').astype('float')
df['number_sold'] = df['number_sold'].str.extract('(\d+)')
df['if_is_shipping'] = df['if_is_shipping'].str.replace("[",'')
df['if_is_shipping'] = df['if_is_shipping'].str.replace("]",'')
df['if_is_shipping'] = df['if_is_shipping'].str.replace("'",'')
is_free_shipping = df['if_is_shipping'] == 'Free Shipping'
df['if_is_shipping'] = np.where(is_free_shipping, '1', '0')
df = df.rename(columns={'if_is_shipping': 'if_is_free_shipping'})
df['store'] = df['store'].str.replace("[",'')
df['store'] = df['store'].str.replace("]",'')
df['store'] = df['store'].str.replace("'",'')
df.to_csv("aliexpress_new.csv", index=False)







