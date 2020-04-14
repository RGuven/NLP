import pandas as pd
from bs4 import BeautifulSoup
import requests


url="https://www.wattpad.com/222204353-tekerlemeler"
r=requests.get(url,headers={"User-Agent":"Rg-Chrome"})
print(r)
source=BeautifulSoup(r.text,"lxml")
print(source.title.text) #TEKERLEMELER - Tekerlemeler - Wattpad


tekerlemeler=source.find_all("div",{"id":"sp222204353-pg1"})
#print(tekerlemeler)
veriler=[]
if r.status_code==200:
    try:
        counter=1
        for tekerleme in tekerlemeler:
    
            tekerleme=tekerleme.find("div").find("pre").find_all("p")
    	    #print(tekerleme)
    	    
            for data in tekerleme:
                data_text=data.text
                #print(data.text)
                counter+=1
                veriler.append(data_text)
        print(counter)
        print(len(veriler))
        print(veriler)
    except AttributeError:
        print("TEXT BULUNAMADI")
else:
    print("""
		****************************
		Sayfa ile bağlantı kurulamadı 
		****************************
          """)   
dict_for_json = { int(i)+44 : veriler[i] for i in range(0, len(veriler) ) }
import json
print(type(dict_for_json)) #type =>dict

with open("tekerleme_data3.json","a",encoding="utf-8") as tekerleme:
    json.dump(dict_for_json,tekerleme,ensure_ascii=False)


