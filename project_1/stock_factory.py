import yfinance

from models import StockModel
from stock import Stock


class StockFactory:
    #TODO what if we enter an invalid ticker?
    #TODO add yesterday's price & today's price, should update based on date
    def make(self, info: StockModel) -> Stock:
        yf_ticker = yfinance.Ticker(info.ticker)
        print(yf_ticker.info)
        company = yf_ticker.info["longName"]
        field = yf_ticker.info["sector"]
        new_stock = Stock(info.ticker, company, field)
        return new_stock
