import requests
from bs4 import BeautifulSoup


def get_data():
    headers = {
        'authority': 'api.rsrv.me',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://www.tury.ru',
        'referer': 'https://www.tury.ru/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&hotel_link=/hotel/id/%HOTEL_ID%&r=769288792',
        headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    hrefs = soup.find_all('a', class_='hotel_name')
    a_list = []
    for item in hrefs:
        result = f"https://www.tury.ru{item.get('href')}"
        print(result)
        a_list.append(result)

    with open('result.txt', 'a') as file:
        for i in a_list:
            file.write(f'{i}\n')








def main():
    get_data()


if __name__ == '__main__':
    main()