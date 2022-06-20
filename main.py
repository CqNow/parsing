import re

import requests
from bs4 import BeautifulSoup
import json
import csv


def get_data():
    """Получение html страницы сайта"""
    url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    req = requests.get(url, headers=headers)
    src = req.text

    """Запись спаршенной страницы в файл"""
    with open('index.html', 'w', encoding='UTF-8') as file:
        file.write(src)

    """Открываем index.html и записываем в переменную src"""
    with open('index.html', 'r', encoding='UTF-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    """Ищем объекты с классом"""
    all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')

    all_categories_dict = {}

    """Записываем название категории и её ссылку в в json"""
    for item in all_products_hrefs:
        item_text = item.text
        item_href = 'https://health-diet.ru' + item.get('href')

        all_categories_dict[item_text] = item_href

    with open('all_categories.json', 'w') as file:
        json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

    """Извлекаем значения из all_categories.json"""
    with open('all_categories.json', 'r') as file:
        all_categories = json.load(file)

    count = 0

    """Переходим по каждой ссылке категории и сохраняем ее в ../data/"""
    for category_name, category_href in all_categories.items():

        """Заменяем символы -,' на нижнее подчеркивание в именах категории"""
        category_name = re.sub("[-,' ]", '_', category_name)
        category_name = re.sub('__', '_', category_name)

        req = requests.get(url=category_href, headers=headers)
        src = req.text

        """Сама запись страницы"""
        with open(f'data/{count}_{category_name}.html', 'w', encoding='UTF-8') as file:
            file.write(src)

        """Открываем страницу категории"""
        with open(f'data/{count}_{category_name}.html', 'r', encoding='UTF-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        """Проверка страницы на наличие таблицы с продуктами"""
        alert_block = soup.find(class_='uk-alert-danger')
        if alert_block is not None:
            continue

        """Забираем заголовки страницы"""
        table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
        product = table_head[0].text
        calories = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text

        with open(f'data/{count}_{category_name}.csv', 'w', encoding='UTF-8') as file:
            writter = csv.writer(file)
            writter.writerow(
                (
                    product,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

        """Забираем данные продуктов"""
        products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

        for item in products_data:
            products_tds = item.find_all('td')

            title = products_tds[0].find('a').text
            calories = products_tds[1].text
            proteins = products_tds[2].text
            fats = products_tds[3].text
            carbohydrates = products_tds[4].text

            """Записываем данные в csv"""

            with open(f'data/{count}_{category_name}.csv', 'a', encoding='UTF-8') as file:
                writter = csv.writer(file)
                writter.writerow(
                    (
                        title,
                        calories,
                        proteins,
                        fats,
                        carbohydrates
                    )
                )

        count += 1


def main():
    get_data()


if __name__ == '__main__':
    main()
