from datetime import datetime
import requests
import json
from bs4 import BeautifulSoup
import time


def get_data():
    all_items = []
    count = 1
    cur_date = datetime.now().strftime('%d_%m_%Y %H_%M')
    for number_page in range(1, 100):
        url = f'https://www.landingfolio.com/api/inspiration?page={number_page}'
        response = requests.get(url=url).text
        if response == '[]':
            break
        json_response = json.loads(response)
        for item in json_response:
            title = item['title'].strip()
            website_url = item['url'].strip()
            images = []
            for image in item['screenshots']:
                image_url = f"https://landingfoliocom.imgix.net/{image['images']['desktop'].strip()}"
                images.append(image_url)
            url = f'https://www.landingfolio.com/inspiration/post/{title.replace(" ", "-")}'
            response = requests.get(url=url)
            soup = BeautifulSoup(response.text, 'lxml')
            try:
                description = soup.find('p', class_='text-base font-normal leading-7 text-gray-600').get_text().strip()
            except:
                print(f'[ERROR] Description not found..')
                description = None
            all_items.append({
                'title' : title,
                'description' : description,
                'website_url' : website_url,
                'image_urls' : images
            })
            print(f'[INFO] {title} added..')
        print(f'[+] Page {count} done..')
        count += 1
    with open(f'result_{cur_date}.json', 'w', encoding='UTF-8') as file:
        json.dump(all_items, file, indent=4, ensure_ascii=False)


def main():
    start_time = time.time()
    get_data()
    print(f'[INFO] Execution time --- {time.time() - start_time}')


if __name__ == '__main__':
    main()
