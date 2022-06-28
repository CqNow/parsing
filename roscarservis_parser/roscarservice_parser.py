import requests
from bs4 import BeautifulSoup
import json


def get_data():
    cookies = {
        'PHPSESSID': 'XfQ3zbte55WsVHM5VYr02vA5u4DI0Kw1',
        'geobase': 'a%3A6%3A%7Bs%3A7%3A%22country%22%3BN%3Bs%3A4%3A%22city%22%3BN%3Bs%3A6%3A%22region%22%3BN%3Bs%3A8%3A%22district%22%3BN%3Bs%3A3%3A%22lat%22%3BN%3Bs%3A3%3A%22lng%22%3BN%3B%7D',
        'selectedCityId': '7273',
        '_ym_uid': '1656159242141890087',
        '_ym_d': '1656159242',
        '_ga': 'GA1.2.7759019.1656159242',
        '_gid': 'GA1.2.573886686.1656159242',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        'BX_USER_ID': '8b73652826481e630121ea7cd1adc23d',
        'recaptcha-init-token': '03AGdBq25PsbQfGllO8D1uBFlbX3crIqoWJVwAC81fr2VgAJ3zz-nVanLaMU-zUiWjBrmG7a869rgdZgZWNQlNQfbVNMa7Z1hGGx0OK5yUIQ4Ho1F4Mq1hrtyECiHzkMhZ7NVIGCcBPMEVlMM5kNrqNNsecmhtuIejkux9UGbaL1PwPdJYwQAJyagfNW-6XRVYNjmVpUvnCDG25XNevBLFZNqF3RFBV6et5pS6GvUYGv6aoI6nuK6x3WwdFiVCjUj2FvFrIq2xq_ui47II-rvzFEpuPlST3xQrSA85YJsxSMGNN-IViSxMnFksmnJHqx5surg9poUwADR6Pg75JVcBeOqmmDbr-HSStIleUNa1XjkuhB3ych6kosj26-rbWkdBvCVmROU5-v4YD4WwuEPkDBRc35tn7WKP4dy0edHrZAKWeqa0uDkc5zV0mnm0piDknWxHc8Bsr3qz',
        'mobileFilterOpened': '0',
        '_gat': '1',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Referer': 'https://roscarservis.ru/catalog/legkovye/?sort%5Bprice%5D=asc&form_id=catalog_filter_form&filter_mode=params&filter_type=tires&diskType=1&arCatalogFilter_458_1500340406=Y&set_filter=Y',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'X-Is-Ajax-Request': 'X-Is-Ajax-Request',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        'https://roscarservis.ru/catalog/legkovye/?sort%5Bprice%5D=asc&form_id=catalog_filter_form&filter_mode=params&filter_type=tires&diskType=1&arCatalogFilter_458_1500340406=Y&set_filter=Y')
    soup = BeautifulSoup(response.text, 'lxml')
    total_page = int(soup.find_all('a', class_='pagination__page')[-1].get_text())

    all_wires = []
    count = 1

    for i in range(1, total_page + 1):
        print(f'Page {i}')
        params = {
            'sort[price]': 'asc',
            'form_id': 'catalog_filter_form',
            'filter_mode': 'params',
            'filter_type': 'tires',
            'diskType': '1',
            'arCatalogFilter_458_1500340406': 'Y',
            'set_filter': 'Y',
            'PAGEN_1': f'{i}',
            'isAjax': 'true',
        }

        response = requests.get('https://roscarservis.ru/catalog/legkovye/', params=params, cookies=cookies,
                                headers=headers)

        items = json.loads(response.text)['items']
        for item in items:
            print(f'Item add {count}')
            store_list = []
            total_amount = 0
            for store in item['commonStores']:
                data_store = {
                    'store_name': store['STORE_NAME'],
                    'store_price': store['PRICE'],
                    'store_amount': store['AMOUNT']
                }
                total_amount += int(store['AMOUNT'])
                store_list.append(data_store)

            data = {
                'name': item['name'],
                'price': item['price'],
                'url': f'https://roscarservis.ru{item["url"]}',
                'img_url': f'https://roscarservis.ru{item["imgSrc"]}',
                'stores': store_list,
                'total_amount': total_amount
            }
            all_wires.append(data)
            count += 1

    with open('result.json', 'a', encoding='UTF-8') as file:
        json.dump(all_wires, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()
