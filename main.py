import requests
from bs4 import BeautifulSoup
import json


def get_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    url = f'https://www.skiddle.com/api/v1/events/search/?limit=41&offset=0&radius=5&minDate=2022-06-23T00%3A00%3A00&maxDate=2023-06-16T23%3A59%3A59&order=trending&latitude=53.958&longitude=-1.081&showVirtualEvents=0&artistmeta=1&artistmetalimit=3&aggs=genreids%2Ceventcode&pub_key=42f25&platform=web&collapse=uniquelistingidentifier'
    response = requests.get(url=url, headers=headers)
    json_data = json.loads(response.text)
    with open('data/result.json', 'a', encoding='UTF-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    with open('data/result.json', encoding='UTF-8') as file:
        src = json.load(file)['results']

    fest_list = []
    count = 0
    for item in src:

        event_name = item['eventname']
        event_date = ' '.join([item['startdate'].split('T')[0], item['startdate'].split('T')[1].split('+')[0]])
        venue_link = item['link']
        print(f'{count=}, {venue_link}')

        try:

            response = requests.get(venue_link).text
            soup = BeautifulSoup(response, 'lxml')
            venue_link = f'https://www.skiddle.com{soup.find("a", class_="tc-white").get("href")}'

            response = requests.get(venue_link).text
            soup = BeautifulSoup(response, 'lxml')
            contact_details = soup.find('h2', string='Venue contact details and info').find_next()
            contact_details = [item.text for item in contact_details.find_all('p')]

            contact_dict = {}

            for item in contact_details:
                contact_details_list = item.split(':')

                if len(contact_details_list) == 3:
                    contact_dict[contact_details_list[
                        0].strip()] = f'{contact_details_list[1].strip()}:{contact_details_list[2].strip()}'
                else:
                    contact_dict[contact_details_list[0].strip()] = contact_details_list[1].strip()

            fest_list.append({
                'Fest name': event_name,
                'Fest date': event_date,
                'Contacts data': contact_dict
            })
        except Exception as ex:
            print(ex)
        count += 1

    with open('data/fest_list.json', 'w', encoding='UTF-8') as file:
        json.dump(fest_list, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()
