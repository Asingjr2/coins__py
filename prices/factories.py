import datetime

import factory
import factory.fuzzy

from .models import Candle, Trade


TRADE_SIDES = (
    ("BUY", "buy"),
    ("SELL", "sell"))
)


class CandleFactory(facotry.django.DjangoModelFactory):
    class Meta:
        model = Candle

    time = factory.fuzzy.FuzzyDateTime(2008, 1, 1, tzinfo=UTC), datetime.datetime.now())
    stock_low = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)
    stock_high = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)
    stock_open = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)
    stock_close = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)
    stock_volume = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)


class TradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Trade

    time = factory.fuzzy.FuzzyDateTime(2008, 1, 1, tzinfo=UTC), datetime.datetime.now())
    trade_id = factory.fuzzy.FuzzyInteger(1, 2000)
    price = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)
    size = factory.fuzzy.FuzzyDecimal(0.0, 1000000, 6)
    side = factory.fuzzy.FuzzyChoice(TRADE_SIDES)
