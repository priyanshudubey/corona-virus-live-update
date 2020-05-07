Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
#This data is scrapped from Ministry of Health and Family Walfare
# So this data is verified and tested. And once the data will be updated on
# Website, it will be update in this script



import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import numpy as np

extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed', 'Cured', 'Death']

response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if stat:
        if len(stat) == 6:
            stat = ['', *stat]
            stats.append(stat)
        elif len(stat) == 5:
            stats.append(stat)
stats[-1][1] = "Total Cases"
stats.remove(stats[-1])
objects = []
for row in stats :
    objects.append(row[1])
    y_pos = np.arange(len(objects))
    performance = []
for row in stats:
    if stat:
        if len(stat) == 6:
            stat = ['', *stat]
            stats.append(stat)
        elif len(stat) == 5:
            stats.append(stat)
    performance.append(int(row[2]) + int(row[3]))

cnfrm_case = []
cnfrm_death = []
cnfrm_cured = []
cnfrm_case.append([int(row[2]) for row in stats])
cnfrm_death.append([int(row[4]) for row in stats])
cnfrm_cured.append([int(row[3]) for row in stats])
c_case = np.sum(cnfrm_case)
c_death = np.sum(cnfrm_death)
c_cured = np.sum(cnfrm_cured)
table = tabulate(stats, headers=SHORT_HEADERS)
print(table)
print('--------------------------------------------------------------------------')
print("Confirm cases in India: "+str(c_case))
print("Confirm deaths in India: "+str(c_death))
print("Confirm cured patients in India: "+str(c_cured)) 