from celery import shared_task
from .models import ScrapingTask
from .coin_market_cap import CoinMarketCap

@shared_task
def scrape_coin_data(coin_name):
    data = CoinMarketCap.fetch_coin_data(coin_name)
    if data:
        task = ScrapingTask.objects.create(coin=coin_name, output=data)
        return task.job_id
    return None

@shared_task
def start_scraping_task(coins):
    job_ids = []
    for coin in coins:
        job_id = scrape_coin_data.delay(coin)
        job_ids.append(job_id)
    return job_ids
