#!/usr/bin/env python
# coding: utf-8

# '''We need to extract a list with all Champions League winners,
# for this purpose Selenium scraping will be used'''

# In[ ]:


get_ipython().run_line_magic('pip', 'install selenium')
from selenium import webdriver


# In[ ]:


get_ipython().run_line_magic('pip', 'install webdriver-manager')
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


from selenium.webdriver.chrome.options import Options

opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
opciones.add_extension('../driver/adblock.crx')       # adblocker
opciones.add_argument('--incognito')


# In[ ]:


PATH=ChromeDriverManager().install()
URL='https://www.worldfootball.net/winner/frauen-champions-league/'
driver=webdriver.Chrome(PATH)
driver.get(URL)

acepto=driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
acepto.click()


# In[ ]:


table = driver.find_element_by_xpath('//*[@id="site"]/div[2]/div[1]/div[1]')
teams = table.find_elements_by_tag_name('tr')


# In[ ]:


lst = []

for i in teams:
    i = i.text.replace('\n', ',').replace('   ', ',,,').split(' ')
    lst.append(i)

lst[0].append('a')
lst[0].append('b')


# In[ ]:


import pandas as pd
import functions as fn


# In[ ]:


col_names=lst[0]
data=lst[1:]
cham=pd.DataFrame(data, columns=col_names)


# In[ ]:


cham = fn.replacing(cham)


# In[ ]:


cham


# In[ ]:


cham.to_csv('./data/champions.csv', index=False)

