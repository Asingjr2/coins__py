from django.core.management.base import BaseCommand, CommandError
from prices.models import Candle, Trade

class Command(BaseCommand):
    """Creating command that will pull data from api automatically."""
    help = "Updates all favorited stocks in DB"

    def update_favorites(self):
        """
        App could pull user favorites stock into DB if favorites exists, or at specific intervals I am guessing?  Are we going to pull all coin data or just a sample of popular ones?

        favorites_list = []
        for stock in favorites_list:
            item_price = client.get_spot_price(currency=stock.currency_code)
            Stock.objects.get(price where name => stock.name) => update stock data

        Not sure if this is something we would do in cache given large potential numbers...
        """
        
        # could be done for all favorites in DB versus one user
        self.stdout.write(self.style.SUCCESS("Updated all favorites")) 
        pass
