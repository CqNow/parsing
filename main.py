import json
import pandas as pd

import requests
from bs4 import BeautifulSoup


def get_data():
    all_data = []
    for i in range(1, 3):
        response = requests.get(f'https://shop.casio.ru/catalog/?PAGEN_1=1{i}')

        soup = BeautifulSoup(response.text, 'lxml')
        all_products = soup.find_all(class_='product-item__link')
        for item in all_products:
            url = f"https://shop.casio.ru{item.get('href')}"
            item_articul = item.find(class_='product-item__articul').text.strip()
            item_brand = item.find(class_='product-item__brand-img').get('alt').strip()
            data = {
                'product_url' : url,
                'product_articul' : item_articul,
                'product_brand' : item_brand
            }
            all_data.append(data)
        with open('result.json', 'w') as file:
            json.dump(all_data, file, indent=4)


def json_to_csv():
    with open('result.json', encoding='UTF-8') as file:
        df = pd.read_json(file)

    df.to_csv('csvfile.csv', encoding='UTF-8', index=False)




def main():
    get_data()
    json_to_csv()


if __name__ == '__main__':
    main()