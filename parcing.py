from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; HandsomeBrowser/1.2)'}
    url = 'https://www.imdb.com/chart/top/' # передаем необходимы URL адрес
    page = requests.get(url, headers=headers)# отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('li', class_='ipc-metadata-list-summary-item') # находим  контейнер с нужным классом
    dictionary = {}
    dictionary['Фильмы'] = {}
    for data in block: # проходим циклом по содержимому контейнера
        if (data.find('h3') and data.find('span',class_='ipc-rating-star--rating')): # находим тег <p>
            FilmName = data.find('h3')
            Rating = data.find('span', class_='ipc-rating-star--rating')
            dictionary['Фильмы'].update({'Название ' + FilmName.text : 'Рейтинг - ' + Rating.text})
    print(dictionary)
parse()