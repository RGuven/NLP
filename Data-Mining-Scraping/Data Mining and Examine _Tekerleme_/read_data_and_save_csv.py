#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:51:29 2019

@author: rguven
"""
import pandas as pd
import json
"""
for i in range(3):
    i=i+1
    with open("tekerleme_data"+str(i)+".json",'r',errors="ignore",encoding="utf-8") as tekerleme:
        data=json.load(tekerleme)
        print(json.dumps(data, indent = 4, sort_keys=True,ensure_ascii=False))
"""


with open("tekerleme_data1.json",'r',errors="ignore",encoding="utf-8") as tekerleme:
        data1=json.load(tekerleme)
        print(json.dumps(data1, indent = 4, sort_keys=True,ensure_ascii=False))
with open("tekerleme_data2.json",'r',errors="ignore",encoding="utf-8") as tekerleme:
        data2=json.load(tekerleme)
        print(json.dumps(data2, indent = 4, sort_keys=True,ensure_ascii=False))
with open("tekerleme_data3.json",'r',errors="ignore",encoding="utf-8") as tekerleme:
        data3=json.load(tekerleme)
        print(json.dumps(data3, indent = 4, sort_keys=True,ensure_ascii=False))
        
        
data_1=pd.DataFrame.from_dict(data1, orient='index')
data_2=pd.DataFrame.from_dict(data2, orient='index')
data_3=pd.DataFrame.from_dict(data3, orient='index')

data_concat=pd.concat([data_1,data_2,data_3])

data_concat.to_csv("tekerlemeler.csv", sep='\t', encoding='utf-8')

df=data_concat

