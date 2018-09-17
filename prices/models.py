from django.db import models


TRADE_SIDES = (
    ("BUY", "buy"),
    ("SELL", "sell"))
)


# Class will be based on request that includes a start, end, and granularity...maybe a form?
class Candle(models.Model):
    time = models.DateTimeField(auto_now=True)
    stock_low = models.DecimalField(max_digits=6, decimal_places=None)
    stock_high = models.DecimalField(max_digits=6, decimal_places=None)
    stock_open = models.DecimalField(max_digits=6, decimal_places=None)()
    stock_close = models.DecimalField(max_digits=6, decimal_places=None)()
    stock_volume = models.DecimalField(max_digits=6, decimal_places=None)()


class Trade(models.Model):
    time = models.DateTimeField(auto_now=True)
    trade_id = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=None)()
    size = models.DecimalField(max_digits=6, decimal_places=None)()
    side = models.CharField(max_length=4, choices=TRADE_SIDES)
