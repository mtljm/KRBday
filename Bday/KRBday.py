#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
import requests as rq
from datetime import datetime, timedelta


# In[13]:


def KRBday():
    url = 'https://finance.naver.com/item/main.naver?code=005930'
    biz_day = rq.get(url=url)
    soup = BeautifulSoup(biz_day.content, "html.parser")
    day = soup.find_all(attrs={'scope':'row'})[0].get_text()
    year = str(datetime.today().year)
    today = datetime.strptime(year+day,'%Y%m/%d')
    if today.timestamp() > datetime.today().timestamp():
        year = today.year-1
        month = today.month
        day = today.day
        today = datetime.strptime(str(year)+str(month)+str(day),'%Y%m%d')

    return today
