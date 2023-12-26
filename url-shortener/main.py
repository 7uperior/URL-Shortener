import os
import requests
from urllib.parse import urlparse


def shorten_link(url, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    endpoint = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(endpoint, headers=headers, json={"long_url": url})
    response.raise_for_status()
    return response.json()["id"]


def count_the_number_of_clicks_on_bitly_link(url, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    parsed_url = urlparse(url)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(endpoint, headers=headers)
    if response.ok:
        return True


def main():
    url = input("Enter the URL: ")

    api_token = os.environ["BITLY_API_TOKEN"]

    try:
        if is_bitlink(url, api_token):
            print(count_the_number_of_clicks_on_bitly_link(url, api_token))
        else:
            print(shorten_link(url, api_token))
    except requests.exceptions.HTTPError:
        print("You have entered an incorrect URL")


if __name__ == "__main__":
    main()
