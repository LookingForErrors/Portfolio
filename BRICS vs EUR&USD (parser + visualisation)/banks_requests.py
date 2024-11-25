import requests as req
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime

# url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'

currencies_dict = {'1030': 'DZD', '1090': 'BYN', '1105': 'BOB',
                   '1115': 'BRL', '1150': 'VND', '1230': 'AED', 
                   '1235': 'USD', '1239': 'EUR', '1240': 'EGP', 
                   '1270': 'INR', '1280': 'IDR', '1300': 'IRR', 
                   '1335': 'KZT', '1375': 'CNY', '1395': 'CUP',
                   '1475': 'MYR', '1520': 'NGN', '1675': 'THB', 
                   '1700J': 'TRY', '1714': 'UGX', '1717': 'UZS',
                   '1800': 'ETB', '1810': 'ZAR'}


def get_date_value_generator(dictionary = currencies_dict):
    for elem in dictionary.keys():
        #собираем url по id валюты
        url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=18/11/2024&VAL_NM_RQ=R0'+elem
        page = req.get(url)
        if page.status_code == 200:
            xml_content = page.content
        
            root = ET.fromstring(xml_content)
            dates = [record.get('Date') for record in root.findall('Record')]
            #перевод дат в формат, необходимый для PostgreSQL
            dates = map(lambda x: datetime.strptime(x, '%d.%m.%Y').strftime('%Y-%m-%d'), dates)

            soup = BeautifulSoup(page.text, "xml")
            values = soup.find_all('Value')
            nominals = soup.find_all('Nominal')
            
            value_list = []
            for i in range(len(values)):
                #некоторые курсы расчитаны на номинал в 10, 100, 1000
                #необходимо нормировать все к единице
                value_list.append(round(float(values[i].text.replace(',' , '.'))/float(nominals[i].text),5))

            val_dict = dict(zip(dates,value_list))

            yield([val_dict, dictionary[elem]])
            
        else:
            print(f"Не удалось извлечь XML. Status code: {page.status_code}")
