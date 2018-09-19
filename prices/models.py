from django.db import models


TRADE_SIDES = (
    ("BUY", "buy"),
    ("SELL", "sell")
)


# Class will be based on request that includes a start, end, and granularity...maybe a form?
class Candle(models.Model):
    item_id = models.CharField(max_length=10)
    base_currency = models.CharField(max_length=10)
    quote_currency = models.CharField(max_length=10)
    item_low = models.DecimalField(max_digits=20, decimal_places=10)
    item_high = models.DecimalField(max_digits=20, decimal_places=10)
    item_open = models.DecimalField(max_digits=20, decimal_places=10)
    item_close = models.DecimalField(max_digits=20, decimal_places=10)
    item_volume = models.DecimalField(max_digits=20, decimal_places=10)
    time_created = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ("item_id", "base_currency", "quote_currency", "time_created"),
        )


class Trade(models.Model):
    time = models.DateTimeField(auto_now=True)
    trade_id = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    size = models.DecimalField(max_digits=20, decimal_places=10)
    side = models.CharField(max_length=4, choices=TRADE_SIDES)
