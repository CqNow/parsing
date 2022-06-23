import requests
import img2pdf


def get_data():
    img_list = []
    """Скачиваем изображения с сайта"""
    for i in range(1, 49):
        response = requests.get(f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg').content
        """Сохраняем их"""
        with open(f'data/{i}.jpg', 'wb') as file:
            file.write(response)
            img_list.append(f'data/{i}.jpg')
            print(f'Download {i} of 48')
    """Сохраняем в pdf"""
    with open('data/recordpower.pdf', 'wb') as file:
        file.write(img2pdf.convert(img_list))

    print('PDF done')

def main():
    get_data()


if __name__ == '__main__':
    main()