import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
cur_date = str(datetime.now().strftime('"%d_%m_%Y_%H_%M"'))


def get_data():
    url = 'https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&otherbooks=1&display=table&page=1'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    last_page = int(soup.find('div', class_='pagination-number').find_all('a')[-1].text)
    all_books = []
    for page in range(1, last_page + 1):
        url = f'https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&otherbooks=1&display=table&page={page}'
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        book_items = soup.find('tbody', class_='products-table__body').find_all('tr')

        for book in book_items:
            book_data = book.find_all('td')

            try:
                book_title = book_data[0].find('a').text.strip()
            except:
                book_title = 'Нет названия книги'

            try:
                book_author = book_data[1].text.strip()
            except:
                book_author = 'Нет автора'

            try:
                book_publisher = book_data[2].find_all('a')
                book_publisher = ":".join([bp.text for bp in book_publisher])
            except:
                book_publisher = 'Нет издательства'

            try:
                book_new_price = book_data[3].find('div', class_='price').find('span').text.strip().replace(' ', '')
            except:
                book_new_price = 'Нет нового прайса'

            try:
                book_old_price = book_data[3].find('span', class_='price-gray').text.strip().replace(' ', '')
            except:
                book_old_price = 'Нет старого прайса'

            try:
                book_discount = round(((book_old_price - book_new_price) / book_old_price) * 100)
            except:
                book_discount = 'Нет скидки'

            try:
                book_status = book_data[-1].text.strip()
            except:
                book_status = 'Нет статуса'

            all_books.append(
                {
                    'book_title': book_title,
                    'book_author': book_author,
                    'book_publishing': book_publisher,
                    'book_current_price': book_new_price,
                    'book_old_price': book_old_price,
                    'book_discount': book_discount,
                    'book_status': book_status
                }
            )

        print(f'[INFO] Page_{page} done..')

    with open(f'result.json', 'w', encoding='UTF-8') as file:
        json.dump(all_books, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()
