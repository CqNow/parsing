import requests
import csv
from datetime import datetime


def get_data():
    t_date = datetime.now().strftime('%d_%m_%Y')

    response = requests.get(url='https://www.lifetime.plus/api/analysis2')

    # with open(f'into_{t_date}.json', 'w', encoding='UTF-8') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    categories = response.json()['categories']
    result = []

    for category in categories:
        category_name = category.get('name').strip()
        category_items = category.get('items')

        for item in category_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_description = item.get('description').strip()
            item_wt = item.get('days')
            item_biomaterial = item.get('biomaterial')

            result.append(
                (category_name, item_name, item_biomaterial, item_description, item_price, item_wt)
            )

    with open(f'result_{t_date}.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Категория',
                'Анализ',
                'Биоматери',
                'Описание',
                'Cтоимость',
                'Готовность(дней)',
            )
        )

        writer.writerows(result)


def main():
    get_data()


if __name__ == '__main__':
    main()
