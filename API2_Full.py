import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def is_bitlink(token, url):
    o = urlparse(url)
    headers = {
        'Authorization': token
    }
    url_full = 'https://api-ssl.bitly.com/v4/bitlinks/' + o.netloc + o.path
    response = requests.get(url_full, headers=headers)
    return response.ok


def shorten_link(token, url):
    headers = {
        'Authorization': token
    }
    data = {
        "long_url": url
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, data=json.dumps(data))
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def count_clicks(token, url):
    o = urlparse(url)
    url_full = 'https://api-ssl.bitly.com/v4/bitlinks/' + o.netloc + o.path + '/clicks'
    headers = {
        'Authorization': token
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.get(url_full, headers=headers, params=params)
    response.raise_for_status()
    cliks = response.json()['link_clicks'][0]['clicks']
    return cliks


if __name__ == '__main__':
    load_dotenv('o.env')
    token = os.environ['TOKEN']
    url = input('Введите ссылку: ')
    if is_bitlink(token, url):
        print('Количество кликов:', count_clicks(token, url))
    else:
        print('Ваш битлинк:', shorten_link(token, url))

