import yfinance

from models import StockModel
from stock import Stock


class StockFactory:
    #TODO what if we enter an invalid ticker?
    #TODO add yesterday's price & today's price, should update based on date
    def make_from_model(self, model: StockModel) -> Stock:
        yf_ticker = yfinance.Ticker(model.ticker)
        # print(yf_ticker.info)
        company = yf_ticker.info["longName"]
        field = yf_ticker.info["sector"]
        long_summary = yf_ticker.info["longBusinessSummary"]
        exchange = yf_ticker.info["exchange"]
        new_stock = Stock(model.ticker, company, field)
        new_stock.set_long_summary(long_summary)
        new_stock.set_exchange(exchange)
        return new_stock
