from django.test import TestCase

import factory

from ..factories import CandleFactory, TradeFactory


class CandleFactoryTestCase(TestCase):
    def test_factory(self):
        candle = CandleFactory()

        self.assertIsNotNone(candle.time)
        self.assertIsNotNone(candle.stock_low)
        self.assertIsNotNone(candle.stock_high)
        self.assertIsNotNone(candle.stock_open)
        self.assertIsNotNone(candle.stock_close)


class TradeFactoryTestCase(TestCase):
    def test_factory(self):
        trade = TradeFactory()

        self.assertIsNotNone(trade.time)
        self.assertIsNotNone(trade.trade_id)
        self.assertIsNotNone(trade.price)
        self.assertIsNotNone(trade.size)
        self.assertIsNotNone(trade.side)
