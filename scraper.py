from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCapScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def scrape_coin(self, coin_acronym):
        url = f"https://coinmarketcap.com/currencies/{coin_acronym.lower()}/"
        self.driver.get(url)
        data = {}
        try:
            data['price'] = self.driver.find_element(By.CSS_SELECTOR, 'div.priceValue').text
        except Exception as e:
            data['error'] = str(e)
        return data

    def close(self):
        self.driver.quit()
