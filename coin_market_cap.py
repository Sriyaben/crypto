# taskmanager/coin_market_cap.py
import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    @staticmethod
    def fetch_coin_data(coin_name):
        url = f"{CoinMarketCap.BASE_URL}{coin_name.lower()}/"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        return CoinMarketCap.parse_coin_data(soup)

    @staticmethod
    def parse_coin_data(soup):
        data = {
            'price': CoinMarketCap.get_price(soup),
            'market_cap': CoinMarketCap.get_market_cap(soup),
            'volume': CoinMarketCap.get_volume(soup),
            # Add more fields as needed
        }
        return data

    @staticmethod
    def get_price(soup):
        return soup.find('div', class_='priceValue').text

    @staticmethod
    def get_market_cap(soup):
        return soup.find('div', class_='statsValue').text

    @staticmethod
    def get_volume(soup):
        return soup.find('div', class_='statsValue').text

    # Add more parsing methods as needed
