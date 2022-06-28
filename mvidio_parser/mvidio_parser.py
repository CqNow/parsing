import requests
import json


def get_data():
    cookies = {
        '__lhash_': 'cde08a05da219710f194b64f24d326cd',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MAIN_PAGE_VARIATION_1': '1',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_2534',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20908068928',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '0200000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '1',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PDP_MAP_DEFAULT': '1',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '10',
        'MVID_REGION_SHOP': 'S906',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '5',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        '_gid': 'GA1.2.921606699.1655647679',
        '_ym_d': '1655647679',
        '_ym_uid': '1655647679525608849',
        'st_uid': '24d08cca381e25438b92db1971dfcd0b',
        'advcake_track_id': 'a4250ff1-3727-b512-e4f0-b224faeb86d5',
        'advcake_session_id': '4229134b-9349-a193-0015-d8921a46ae58',
        'tmr_lvid': 'f911c46a513240990848324ba488208f',
        'tmr_lvidTS': '1655647678906',
        '_ym_isad': '1',
        'uxs_uid': '39afffa0-efd9-11ec-864c-9f57ee8cfbd4',
        'flocktory-uuid': 'a7aff405-b3e8-43b2-b050-c4f258b5ff34-3',
        'afUserId': '8a8bd03b-eddb-4830-be47-d4b6fc70ed67-p',
        'AF_SYNC': '1655647679837',
        'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
        'bIPs': '434929338',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '1812257802.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrTShnLRUlOWZZaBg7Szg9fSltHh4KP2MILzEMbF4LF1tJSl1kR2A8LEgKKhEtUhdjWxJFGjxtIGFQWSJDWlNqJh8WfHEnVg0TZEZHdmUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5BaSRmR18kR1lJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=KMvveQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrTShnLRUlOWZZaBg7Szg9fSltHh4KP2MILzEMbF4LF1tJSl1kR2A8LEgKKhEtUhdjWxJFGjxtIGFQWSJDWlNqJh8WfHEnVg0TZEZHdmUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5BaSRmR18kR1lJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=KMvveQ==',
        'cfidsgib-w-mvideo': 'iXgB7h0cGtLnUpfEc5/LvVHGWqsEW/cesRrIc4XJYAUO5GrnKVrN5awR+FeZXtxmwYGMawrQbK6aY9KCZJJ85yq421GnagzLVbvM1v5fTfyaqLyanMlT9cPtfaFL7Z8RSL9fS0KevYtx9Fdqq+F5MuZU61MxEPTHPyi3',
        'cfidsgib-w-mvideo': 'iXgB7h0cGtLnUpfEc5/LvVHGWqsEW/cesRrIc4XJYAUO5GrnKVrN5awR+FeZXtxmwYGMawrQbK6aY9KCZJJ85yq421GnagzLVbvM1v5fTfyaqLyanMlT9cPtfaFL7Z8RSL9fS0KevYtx9Fdqq+F5MuZU61MxEPTHPyi3',
        'gsscgib-w-mvideo': 'qWPlUKKeXRfp253i51wHBXRK0Nz0crF2K/hVjysswZQ1d850oIb04QgDqH/wANO3N2UNELQTOT92PyXAhBH6Z4ThoXkyCVT2WI/uiWGT4iZ0Uy/nIBo1q9SEuHyNVduv0HhX8CVXAN+6Ab73RtN/JtUhy788B9coU7eTYCZ8Z0eGMY6nDiBFQK2VJtnWSRr7/DNzRCZPp31SOyBVDori1HxTlvQ/QTTGvI0nD20Wna5OFwIgEeBusThW9cbNlA==',
        'gsscgib-w-mvideo': 'qWPlUKKeXRfp253i51wHBXRK0Nz0crF2K/hVjysswZQ1d850oIb04QgDqH/wANO3N2UNELQTOT92PyXAhBH6Z4ThoXkyCVT2WI/uiWGT4iZ0Uy/nIBo1q9SEuHyNVduv0HhX8CVXAN+6Ab73RtN/JtUhy788B9coU7eTYCZ8Z0eGMY6nDiBFQK2VJtnWSRr7/DNzRCZPp31SOyBVDori1HxTlvQ/QTTGvI0nD20Wna5OFwIgEeBusThW9cbNlA==',
        'fgsscgib-w-mvideo': 'trA2aa3b26848c5fd59b83ff8243e398c61ed82d',
        'fgsscgib-w-mvideo': 'trA2aa3b26848c5fd59b83ff8243e398c61ed82d',
        'cfidsgib-w-mvideo': 'n4/daQ+OpCc2VpaGP+oV0EdRr/1gDsDn/xSHT7A6N2M/X16pTZ4i6vdpiiKgn6ZVb8difCrCHbJHRlV0Og5hYfRKb6xsYg5EJ98z41fMGhuTHsznGZQY7nz6Hrv3rSHa7nnHf1EIPPJvB/WW59jCcRCdLTcEXaP9IRT9',
        'CACHE_INDICATOR': 'false',
        'mindboxDeviceUUID': '912d5e30-5e8f-4fc8-a543-0b2cccc0c6fd',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22912d5e30-5e8f-4fc8-a543-0b2cccc0c6fd%22%7D',
        'MVID_ENVCLOUD': 'primary',
        '_ga_CFMZTSS5FM': 'GS1.1.1655647678.1.1.1655649459.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1655647678.1.1.1655649459.60',
        '_dc_gtm_UA-1873769-1': '1',
        '_ga': 'GA1.2.509461094.1655647679',
        '_dc_gtm_UA-1873769-37': '1',
        'tmr_detect': '1%7C1655649459912',
        'tmr_reqNum': '48',
        'JSESSIONID': 'Qy2Tvv0VFTbNvJWhDv2VsQLKf9vd5Fp9b4W2smpS5hTKJP78X6rZ!1832903056',
        'ADRUM_BT': 'R:98|g:56e6ffc7-4c65-4f07-847e-3766675179866059660',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=cde08a05da219710f194b64f24d326cd; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MAIN_PAGE_VARIATION_1=1; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2534; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20908068928; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=0200000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PDP_MAP_DEFAULT=1; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=10; MVID_REGION_SHOP=S906; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; _gid=GA1.2.921606699.1655647679; _ym_d=1655647679; _ym_uid=1655647679525608849; st_uid=24d08cca381e25438b92db1971dfcd0b; advcake_track_id=a4250ff1-3727-b512-e4f0-b224faeb86d5; advcake_session_id=4229134b-9349-a193-0015-d8921a46ae58; tmr_lvid=f911c46a513240990848324ba488208f; tmr_lvidTS=1655647678906; _ym_isad=1; uxs_uid=39afffa0-efd9-11ec-864c-9f57ee8cfbd4; flocktory-uuid=a7aff405-b3e8-43b2-b050-c4f258b5ff34-3; afUserId=8a8bd03b-eddb-4830-be47-d4b6fc70ed67-p; AF_SYNC=1655647679837; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; bIPs=434929338; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1812257802.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrTShnLRUlOWZZaBg7Szg9fSltHh4KP2MILzEMbF4LF1tJSl1kR2A8LEgKKhEtUhdjWxJFGjxtIGFQWSJDWlNqJh8WfHEnVg0TZEZHdmUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5BaSRmR18kR1lJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=KMvveQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UrTShnLRUlOWZZaBg7Szg9fSltHh4KP2MILzEMbF4LF1tJSl1kR2A8LEgKKhEtUhdjWxJFGjxtIGFQWSJDWlNqJh8WfHEnVg0TZEZHdmUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5BaSRmR18kR1lJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=KMvveQ==; cfidsgib-w-mvideo=iXgB7h0cGtLnUpfEc5/LvVHGWqsEW/cesRrIc4XJYAUO5GrnKVrN5awR+FeZXtxmwYGMawrQbK6aY9KCZJJ85yq421GnagzLVbvM1v5fTfyaqLyanMlT9cPtfaFL7Z8RSL9fS0KevYtx9Fdqq+F5MuZU61MxEPTHPyi3; cfidsgib-w-mvideo=iXgB7h0cGtLnUpfEc5/LvVHGWqsEW/cesRrIc4XJYAUO5GrnKVrN5awR+FeZXtxmwYGMawrQbK6aY9KCZJJ85yq421GnagzLVbvM1v5fTfyaqLyanMlT9cPtfaFL7Z8RSL9fS0KevYtx9Fdqq+F5MuZU61MxEPTHPyi3; gsscgib-w-mvideo=qWPlUKKeXRfp253i51wHBXRK0Nz0crF2K/hVjysswZQ1d850oIb04QgDqH/wANO3N2UNELQTOT92PyXAhBH6Z4ThoXkyCVT2WI/uiWGT4iZ0Uy/nIBo1q9SEuHyNVduv0HhX8CVXAN+6Ab73RtN/JtUhy788B9coU7eTYCZ8Z0eGMY6nDiBFQK2VJtnWSRr7/DNzRCZPp31SOyBVDori1HxTlvQ/QTTGvI0nD20Wna5OFwIgEeBusThW9cbNlA==; gsscgib-w-mvideo=qWPlUKKeXRfp253i51wHBXRK0Nz0crF2K/hVjysswZQ1d850oIb04QgDqH/wANO3N2UNELQTOT92PyXAhBH6Z4ThoXkyCVT2WI/uiWGT4iZ0Uy/nIBo1q9SEuHyNVduv0HhX8CVXAN+6Ab73RtN/JtUhy788B9coU7eTYCZ8Z0eGMY6nDiBFQK2VJtnWSRr7/DNzRCZPp31SOyBVDori1HxTlvQ/QTTGvI0nD20Wna5OFwIgEeBusThW9cbNlA==; fgsscgib-w-mvideo=trA2aa3b26848c5fd59b83ff8243e398c61ed82d; fgsscgib-w-mvideo=trA2aa3b26848c5fd59b83ff8243e398c61ed82d; cfidsgib-w-mvideo=n4/daQ+OpCc2VpaGP+oV0EdRr/1gDsDn/xSHT7A6N2M/X16pTZ4i6vdpiiKgn6ZVb8difCrCHbJHRlV0Og5hYfRKb6xsYg5EJ98z41fMGhuTHsznGZQY7nz6Hrv3rSHa7nnHf1EIPPJvB/WW59jCcRCdLTcEXaP9IRT9; CACHE_INDICATOR=false; mindboxDeviceUUID=912d5e30-5e8f-4fc8-a543-0b2cccc0c6fd; directCrm-session=%7B%22deviceGuid%22%3A%22912d5e30-5e8f-4fc8-a543-0b2cccc0c6fd%22%7D; MVID_ENVCLOUD=primary; _ga_CFMZTSS5FM=GS1.1.1655647678.1.1.1655649459.0; _ga_BNX5WPP3YK=GS1.1.1655647678.1.1.1655649459.60; _dc_gtm_UA-1873769-1=1; _ga=GA1.2.509461094.1655647679; _dc_gtm_UA-1873769-37=1; tmr_detect=1%7C1655649459912; tmr_reqNum=48; JSESSIONID=Qy2Tvv0VFTbNvJWhDv2VsQLKf9vd5Fp9b4W2smpS5hTKJP78X6rZ!1832903056; ADRUM_BT=R:98|g:56e6ffc7-4c65-4f07-847e-3766675179866059660',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-set-application-id': '122d3ce3-9aef-41eb-a548-98eff8c5ae53',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
