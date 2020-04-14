"biraz daha uğraşılacak"
import pandas as pd
from bs4 import BeautifulSoup
import requests


url="https://mbirgin.com/?c=Cevap&TopicID=1102&t=ensevilentekerlemelersesli&v=XObmRf3VhcE#v=XObmRf3VhcE"

r=requests.get(url,headers={"User-Agent":"Rg-Chrome"})
print(r)
source=BeautifulSoup(r.text,"lxml")
print(source.title.text) 
data=[]
if r.status_code==200:
    try:
        tekerlemeler=source.find_all("div",{"id":"divContent"})
        #print(tekerlemeler)
        counter=1
        for tekerle in tekerlemeler:
            tekerle=tekerle.find("div",{"class":"cssQuote tonguetwister"})
            print(tekerle.text)
            appending=tekerle.text
            data.append(appending)
            counter+=1
        print(counter)

    except AttributeError:
        print("TEXT BULUNAMADI")
else:
    print("""
		****************************
		Sayfa ile bağlantı kurulamadı 
		****************************
          """)

print(len(data))
print(type(data))

for i,v in enumerate(data):
    dict_for_json1={i:v}
    print(i,v)
print(type(dict_for_json1),"----------------------")

import json

#list => dict => json => save
dict_for_json = { int(i)+35 : data[i] for i in range(0, len(data) ) }

print(type(dict_for_json)) #type =>dict


with open("tekerleme_data2.json","a",encoding="utf-8") as tekerleme:
     json.dump(dict_for_json,tekerleme,ensure_ascii=False)








