# Replace empty migration file data with below and uncomment model import
from django.db import migrations

import requests

# from ..models import Candle

def update_bitcoin_prices(apps, schema_editor):
    """Data load for Bitcoin daily price data.

    Pulling data from coinbase sandbox api to seed database.
    """
    coin_currency_sets = ["BTC-USD", "BTC-EUR"]
    for coin_set in coin_currency_sets:
        url = "https://api-public.sandbox.pro.coinbase.com/products/{}/candles?granularity=86400".format(coin_set)
        r = requests.get(url)
        response = r.json()
        
        # Seeding DB with Bitcoin response data and seperating coin_set info.
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


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_bitcoin_prices),
    ]

