import bs4
import requests

res=requests.get("https://www.brainyquote.com/quote_of_the_day.html")
print(res)
soup=bs4.BeautifulSoup(res.text,'lxml')

quote=soup.find('img',{"class":"p-qotd"})
print(quote)

msg=quote['alt']
print("Message of the day =", msg)

photo_url="https://www.brainyquote.com/"+quote['data-img-url']
res=requests.get(photo_url)

import datetime
date=datetime.datetime.now().date()
file_name=str(date)+".jpeg"
with open("p1.jpeg","wb") as f:
    f.write(res.content)