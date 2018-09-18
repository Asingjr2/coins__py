from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from datetime import datetime

import requests
from coinbase.wallet.client import Client

from .models import Candle

class HomeView(TemplateView):
    template_name = "prices/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        client = Client("YOUR_INFO","YOUR_INFO", api_version="2018-09-15" )
        currency_code = "USD"
        item_price = client.get_spot_price(currency=currency_code)
        print("Last price was {}".format(item_price.amount))
        context["price"] = item_price.amount

        # URL sandbox content
        url = "https://api-public.sandbox.pro.coinbase.com/products/BTC-USD/candles?granularity=300"
        r = requests.get(url)
        context["json_stuff"] = r.json() 
        return context

# Returned time is ISO 8601
