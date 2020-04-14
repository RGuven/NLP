import pandas as pd
from bs4 import BeautifulSoup
import requests


url="https://www.ilkokuldokumanlari.com/zor-tekerlemeler/"
r=requests.get(url,headers={"User-Agent":"Rg-Chrome"})
print(r)
source=BeautifulSoup(r.text,"lxml")
print(source.title.text) #Söylenmesi Zor Tekerlemeler | İlkokul Dokümanları



tekerlemeler_info=source.find_all('div',{"class":"bs-shortcode-alert alert alert-info"})
tekerlemeler_success=source.find_all('div',{"class":"bs-shortcode-alert alert alert-success"})
#print(tekerlemeler_success)
#print(tekerlemeler_info)

data=[]

for tekerleme_infoo in tekerlemeler_info:
    tekerleme=tekerleme_infoo.find("span").text
    print(tekerleme)
    data.append(tekerleme)

for tekerlemeler_successs in tekerlemeler_success:
    tekerleme=tekerlemeler_successs.find("span").text
    print(tekerleme)
    data.append(tekerleme)

print("TOPLAM TEKERLEME SAYISI "+str(len(data)))


#Save Json

import json

#list => dict => json => save
dict_for_json = { i : data[i] for i in range(0, len(data) ) }

print(type(dict_for_json)) #type =>dict



with open("tekerleme_data1.json","w",encoding="utf-8") as tekerleme:
     json.dump(dict_for_json,tekerleme,ensure_ascii=False)





