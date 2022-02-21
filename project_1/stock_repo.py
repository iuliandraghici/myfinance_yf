import json
from stock import Stock
from exceptions import StockNotFound
from stock_factory import StockFactory


class StockRepository:
    def __init__(self):
        self.stocks = {}
        # self.__load()

    def add(self, new_stock: Stock):
        self.stocks[new_stock.ticker] = new_stock
        self.__save()

    def get_all(self) -> list[Stock]:
        return list(self.stocks.values())

    # if we do not have the stock, we can raise an error or return None
    def get_by_ticker(self, ticker: str) -> Stock:
        if ticker in self.stocks.keys():
            return self.stocks[ticker]
        else:
            raise StockNotFound()
        # return StockFactory().make_extended_stock(ticker)

    def remove(self, stock_id: str):
        self.stocks.pop(stock_id)
        self.__save()

    def load(self):
        file = open("database.txt")
        json_items = file.read()
        file.close()
        items = json.loads(json_items)
        # items = list of dictionaries from the file
        for one_item in items:
            new_stock = Stock(one_item["ticker"], one_item["company"], one_item["field"], one_item["amount"])
            if "longSummary" in one_item and "exchange" in one_item:
                new_stock.set_long_summary(one_item["longSummary"])
                new_stock.set_exchange(one_item["exchange"])
            self.stocks[one_item["ticker"]] = new_stock

    def __save(self):
        list_json = json.dumps([{
            "ticker": x.ticker,
            "company": x.company,
            "amount": x.amount,
            "field": x.field,
            "longSummary": x.long_summary,
            "exchange": x.exchange,
        } for x in self.stocks.values()], indent=2)
        file = open("database.txt", "w")
        file.write(list_json)
        file.close()
