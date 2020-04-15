import requests
from bs4 import BeautifulSoup

#根据steam网页的命名规则

url = "https://store.steampowered.com/search/?specials=1&specials=1"+"&os=win"
s = requests.session()
res = s.get(url).text
'''print(res)'''
soup = BeautifulSoup(res, "html.parser")
contents = soup.find_all('a',class_='search_result_row ds_collapse_flag')
print(contents)
for content in contents:
    try:
        name = content.find(class_="title").string.strip()
        '''date = content.find("div",class_="col search_released responsive_secondrow").string.strip()'''
        discount=content.find("span").string.strip()
        '''price= content.find("div",class_="col search_price discounted responsive_secondrow").string.strip()'''
        img_src = content.find("div",class_="col search_capsule").find('img').get("src")
        href=content.get("href")
        '''print(name,href,discount,img_src+'\n')'''
    except:
        print("error")