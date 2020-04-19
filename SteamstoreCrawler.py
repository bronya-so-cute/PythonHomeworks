import requests
from bs4 import BeautifulSoup

#根据steam网页的命名规则

url = "https://store.steampowered.com/search/?specials=1&specials=1"+"&os=win"
s = requests.session()
res = s.get(url).text
soup = BeautifulSoup(res, "html.parser")
contents = soup.find_all('a',class_='search_result_row ds_collapse_flag')
for content in contents:
    try:
        name = content.find(class_="title").string.strip()
        date = content.find("div",class_="col search_released responsive_secondrow").string.strip()
        discount=content.find("div",class_="col search_discount responsive_secondrow").find('span').string.strip()
        price=content.find("div",class_="col search_price_discount_combined responsive_secondrow").get("data-price-final")
        price=int(price)
        price=price/100
        Originalprice= content.find("strike").string.strip()
        img_src = content.find("div",class_="col search_capsule").find('img').get("src")
        href=content.get("href")
        print(name,"/",date,"/",discount,"/",Originalprice,'-> ¥',price,"/",href,"/",img_src+'\n')
    except:
        continue
