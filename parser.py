from bs4 import BeautifulSoup
import requests
import re
headers={'тут хидр '}
url1="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
def parse(url1,headers):
    h=[]
    h2=[]
    global title
    title=''
    session=requests.Session()
    request=session.get(url1,headers=headers)
    if request.status_code==200:
        soup=BeautifulSoup(request.content,'html.parser')
        divs=soup.find_all('article',class_="place")
        for div in divs:
            
          title=div.find_all('div',class_='small-3 columns')
        for k in title:
            q=k.find('a').text
            h.append(k.find('i'))
            print(q)

    else:
        print('net')
    for qwe in h:
        h2.append(re.sub('[<i class="schedule__genre">,</i>]','',str(qwe)))
    print(h2)
        

parse(url1,headers)

    

