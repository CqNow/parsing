import requests
from bs4 import BeautifulSoup
import json


def get_data():
    """Получаем все url"""
    first_url = 'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true'
    all_urls = [first_url, ]
    persons_url_list = []
    for i in range(12, 733, 20):
        url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
        all_urls.append(url)

    """Получаем url на каждого человека"""
    for url in all_urls:
        response = requests.get(url)
        result = response.content

        soup = BeautifulSoup(result, 'lxml')
        persons = soup.find_all(class_='bt-open-in-overlay')

        for person in persons:
            person_page_url = person.get('href')
            persons_url_list.append(person_page_url)

    """Записываем url'ы в файл"""
    with open('persons_all_url.txt', 'a') as file:
        for person_url in persons_url_list:
            file.write(f'{person_url}\n')

    """Отправляем запрос по каждой ссылке, забираем значение content и записываем в файл"""
    with open('persons_all_url.txt') as file:
        src = [line.strip() for line in file.readlines()]

    all_response = []

    for i in src:
        response = requests.get(i).content
        all_response.append(response)

    with open('test.txt', 'a') as file:
        for item in all_response:
            file.write(f'{item}\n')


    with open('test.txt') as file:
        src = [line.strip() for line in file.readlines()]

    data_list = []
    count = 0
    for response in src:
        print(count)
        soup = BeautifulSoup(response, 'lxml')
        person_name_company = soup.find(class_='bt-biografie-name').find('h3').text.replace('\\n', '').strip()
        print(person_name_company)
        person_name = person_name_company.split(',')[0].strip()
        person_company = person_name_company.split(',')[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')
        all_urls_networks = []
        for item in social_networks:
            all_urls_networks.append(item.get('href'))

        data = {
            'person_name' : person_name,
            'company_name' : person_company,
            'social_networks' : all_urls_networks
        }
        data_list.append(data)
        count += 1


    with open('all_persons.json', 'w') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def main():
    get_data()

if __name__ == '__main__':
    main()