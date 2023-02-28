import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def is_bitlink(token, url):
    divided_url = urlparse(url)
    header = {
        'Authorization': token
    }
    full_url = f'https://api-ssl.bitly.com/v4/bitlinks/ {divided_url.netloc} {divided_url.path}'
    response = requests.get(full_url, headers=header)
    return response.ok


def shorten_link(token, url):
    header = {
        'Authorization': token
    }
    long_url = {
        "long_url": url
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=header, json=long_url)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def count_clicks(token, url):
    divided_url = urlparse(url)
    full_url = f'https://api-ssl.bitly.com/v4/bitlinks/ {divided_url.netloc} {divided_url.path} {"/clicks"}'
    print(full_url)
    print(divided_url.netloc)
    print(divided_url.path)
    header = {
        'Authorization': token
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.get(full_url, headers=header, params=params)
    response.raise_for_status()
    cliks = response.json()['link_clicks'][0]['clicks']
    return cliks


def main():
    if __name__ == '__main__':
        load_dotenv('ID.env')
        token = os.environ['BITLINK_TOKEN']
        url = input('Введите ссылку: ')
        if is_bitlink(token, url):
            print('Количество кликов:', count_clicks(token, url))
        else:
            print('Ваш битлинк:', shorten_link(token, url))


main()
