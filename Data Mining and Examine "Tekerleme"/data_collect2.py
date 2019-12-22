"Look Again"
import pandas as pd
from bs4 import BeautifulSoup
import requests


url="https://www.shallwe.com.tr/soylemesi-zor-ve-uzun-tekerlemeler/"
r=requests.get(url,headers={"User-Agent":"Rg-Chrome"})
print(r)
source=BeautifulSoup(r.text,"lxml")
print(source.title.text) 

if r.status_code==200:
    pass

else:
    print("""
		****************************
		Sayfa ile bağlantı kurulamadı 
		****************************
	 """)



tekerlemeler=source.find('div',{"class":"entry-content g1-typography-xl"})
print(tekerlemeler)
print(type(tekerlemeler)) #bs4.element.tag

data=[]
for tekerle in tekerlemeler:
    tekerle=tekerle.find("p")
    print(tekerle)
    #data.append(tekerle)


            


print(len(data))
print(data)


