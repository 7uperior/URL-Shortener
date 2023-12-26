import os
import requests
from urllib.parse import urlparse


def shorten_link(url, token_api):
    headers = {"Authorization": f"Bearer {token_api}"}
    endpoint = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(endpoint, headers=headers, json={"long_url": url})
    response.raise_for_status()
    return response.json()["id"]


def count_the_number_of_clicks_on_bitly_link(url, token_api):
    headers = {"Authorization": f"Bearer {token_api}"}
    endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, token_api):
    headers = {"Authorization": f"Bearer {token_api}"}
    parsed_url = urlparse(url)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return True


def main():
    url = input("Введите ссылку: ")
    token_api = os.environ["TOKEN_API_BITLY"]

    try:
        if is_bitlink(url, token_api):
            print(count_the_number_of_clicks_on_bitly_link(url, token_api))
        else:
            print(shorten_link(url, token_api))
    except requests.exceptions.HTTPError:
        print("Вы ввели некорректную ссылку")


if __name__ == "__main__":
    main()
