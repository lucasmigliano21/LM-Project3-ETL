# '''We need to extract a list with all Champions League winners,
# for this purpose Selenium scraping will be used'''

get_ipython().run_line_magic('pip', 'install selenium')

from selenium import webdriver

get_ipython().run_line_magic('pip', 'install webdriver-manager')

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
opciones.add_extension('../driver/adblock.crx')       # adblocker
opciones.add_argument('--incognito')


PATH=ChromeDriverManager().install()
URL='https://www.worldfootball.net/winner/frauen-champions-league/'
driver=webdriver.Chrome(PATH)
driver.get(URL)
acepto=driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
acepto.click()

table = driver.find_element_by_xpath('//*[@id="site"]/div[2]/div[1]/div[1]')
teams = table.find_elements_by_tag_name('tr')

lst = []

for i in teams:
    i = i.text.replace('\n', ',').replace('   ', ',,,').split(' ')
    lst.append(i)

lst[0].append('a')
lst[0].append('b')

import pandas as pd
import functions as fn

col_names=lst[0]
data=lst[1:]
cham=pd.DataFrame(data, columns=col_names)
cham = fn.replacing(cham)

cham.to_csv('./data/champions.csv', index=False)