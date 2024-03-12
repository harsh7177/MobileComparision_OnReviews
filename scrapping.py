import requests
from bs4 import BeautifulSoup as bs
import streamlit as st
import pandas as pd


@st.cache_data
def scrap(product):
    Item_name=[]
    Item_href=[]
    Item_Price=[]
    Item_Image=[]
    li_lists=[]
    main_url='https://www.flipkart.com'
    url='https://www.flipkart.com/search?q={}'.format(product)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com/',
    'Cache-Control': 'max-age=0',
}

    scrap=requests.get(url=url,headers=headers)
    data=bs(scrap.text,'html.parser')
    [Item_name.append(i.text) for i in data.find_all('div',class_='_4rR01T')[0:2]]
    try:
        [Item_Price.append(float(i.text.replace("₹",'').replace(',',''))) for i in data.find_all('div',class_='_25b18c')[0:2]]
        divs = data.find_all('div', class_='fMghEO')
        for div in divs:
            li_elements = div.find_all('li')
            li_texts = [li.text.strip() for li in li_elements]
            li_lists.append(li_texts)
    except:
        [Item_Price.append(float(i.text.split('₹')[1].replace(',',''))) for i in data.find_all('div',class_='_25b18c')[0:2]]
        divs = data.find_all('div', class_='fMghEO')
        for div in divs:
            li_elements = div.find_all('li')
            li_texts = [li.text.strip() for li in li_elements]
            li_lists.append(li_texts)
    for i in data.find_all('div', class_='CXW8mj')[0:2]:
        img_tag = i.find('img')
        src = img_tag['src']
        Item_Image.append(src)
    
    for i in data.find_all('a',class_='_1fQZEK')[0:2]:
        Item_href.append((main_url+i.get('href').replace('/p/','/product-reviews/')))
    df=pd.DataFrame(zip(Item_Price,Item_name,Item_href,Item_Image,li_lists),columns=['Price','Variant','href','Image','Details'])
    return df
@st.cache_data
def review_scrap(href):
    reviews=[]
    rating=[]
    rev_url=href
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    rev_scrap=requests.get(url=rev_url,headers=headers)
    rev_data=bs(rev_scrap.text,'html.parser')
    try:
        rev_pages=int(rev_data.find_all('div',class_='_2MImiq _1Qnn1K')[0].text.split('123456')[0].split('of')[-1].strip())
    except:
        rev_pages=rev_data.find_all('div',class_='_2MImiq _1Qnn1K')[0].text.split('123456')[0].split('of')[-1].strip()
        rev_pages=int(rev_pages.replace(',',''))

    for i in range(rev_pages)[1:200]:
        try:
            if i%10==0:
                continue
            else:  
                rev_page_href=rev_url+'&=30&page={}'.format(i)
                reviews_scrap=requests.get(url=rev_page_href,headers=headers)
                reviews_data=bs(reviews_scrap.text,'html.parser')
                for i in reviews_data.find_all('div',class_='_1AtVbE col-12-12')[4:]:
                    try:
                        rating.append(int(i.text.split('READ MORE')[0][:1]))
                        reviews.append(i.text.split('READ MORE')[0][1:])
                    except:
                        continue
                    
        except:
            continue
    review_df=pd.DataFrame(zip(reviews,rating),columns=['Review','Rating'])
    return review_df
@st.cache_data    
def review_analysis(data):
    st.write(data)

def anime(url:str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return(r.json)
    
    
