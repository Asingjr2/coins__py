# Management command to simulate updates to DB.

from django.core.management.base import BaseCommand, CommandError
from prices.models import Candle, Trade

import requests

from prices.models import Candle

class Command(BaseCommand):
    """Creating command that will pull data from api automatically."""
    help = "Updates all favorited stocks in DB"

    def handle(self, *args, **options):
        """Simulating an api request to coinbase for updated price information. 

        Utilizing same method in migration to pull updated coinbase api information into app db.
        This command uses sandbox environment without unique api for real time data.
        """
        coin_currency_sets = ["BTC-USD", "BTC-EUR", "LTC-EUR", "ETH-EUR" ]

        for coin_set in coin_currency_sets:
            url = "https://api-public.sandbox.pro.coinbase.com/products/{}/candles?granularity=86400".format(coin_set)
            r = requests.get(url)
            response = r.json()
            
            # Info below creates new items since price and other transaction data will change daily
            coin_curr = coin_set.split("-")
            for candle in response:
                new_candle = Candle.objects.create(
                    item_id = 90, 
                    base_currency = coin_curr[0],
                    quote_currency = coin_curr[1], 
                    item_low = candle[1], 
                    item_high = candle[2],
                    item_open = candle[3],
                    item_close = candle[4], 
                    item_volume = candle[5],
                ) 
                new_candle.save()   
