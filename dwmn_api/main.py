import os
import requests
from urllib.parse import urlparse


def shorten_link(url, token_api):
    headers = {"Authorization": f"Bearer {token_api}"}
    bitly_new_link_endpoint = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(
        bitly_new_link_endpoint, headers=headers, json={"long_url": url}
    )
    response.raise_for_status()
    return response.json()["id"]


def count_the_number_of_clicks_on_bitly_link(url, token_api):
    headers = {"Authorization": f"Bearer {token_api}"}
    bitly_summary_endpoint = (
        f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"
    )
    response = requests.get(bitly_summary_endpoint, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, token_api):
    headers = {"Authorization": f"Bearer {token_api}"}
    parsed_url = urlparse(url)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    bitly_check_endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(bitly_check_endpoint, headers=headers)
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
