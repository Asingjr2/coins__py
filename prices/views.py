from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

import requests
from coinbase.wallet.client import Client

class HomeView(TemplateView):
    template_name = "prices/home.html"

    # Need api version

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        client = Client("faI9AZCIVvQTnsgC","aVpg014O6sXrFq8GSD1sSqU2XAhyGpg2", api_version="2018-09-15" )
        currency_code = "USD"
        item_price = client.get_spot_price(currency=currency_code)
        print("Last price was {}".format(item_price.amount))
        context["price"] = item_price.amount
        
        return context

