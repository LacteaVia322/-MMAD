import requests
from bs4 import BeautifulSoup
import re
import numpy as np

URL = 'https://auto.ru/cars/ferrari/all/'

def get_html(url, params=None):
    return requests.get('https://auto.ru/cars/ferrari/all/')

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ListingItem-module__main')
    cars = []
    prices = []
    for item in items:
        cars.append({
            'Марка': item.find('h3', class_='ListingItemTitle-module__container ListingItem-module__title').get_text(strip=True),
            'Ссылка на авто': item.find('a', class_='Link ListingItemTitle-module__link').get('href'),
            'Цена': int(''.join(map(str, re.findall(r'\d*\.\d+|\d+', str(item.find('div', class_='ListingItemPrice-module__content').get_text(strip=True)))))),
            'Год выпуска': item.find('div', class_='ListingItem-module__column ListingItem-module__columnMiddle').get_text(),
        })
        prices.append(int(''.join(map(str, re.findall(r'\d*\.\d+|\d+', str(item.find('div', class_='ListingItemPrice-module__content').get_text(strip=True)))))))
    output(cars,prices)
    return cars

def output(cars,prices):
    print('Предложенные автомобили марки "Ferrari" ', cars, '\n')    
    print('Количество машин марки "Ferrari" ' + str(len(cars)) + '\n')
    print('Средняя цена автомобиля марки "Ferrari" ' + str(np.mean(prices))  + '\n')
    print('Максимальная цена автомобиля марки "Ferrari" ' + str(np.max(prices))  + '\n')

html = get_html(URL)
if html.status_code == 200:
    cars = get_content(html.text)
else:
    print('Error')
    
