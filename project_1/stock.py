
class Stock:

    def __init__(self, ticker: str, company_name: str, field: str, amount: float = 0):
        self.ticker = ticker
        self.company = company_name
        self.field = field
        self.amount = amount
        self.long_summary = ""
        self.exchange = ""

    def set_long_summary(self, summary: str):
        self.long_summary = summary

    def set_exchange(self, exchange: str):
        self.exchange = exchange
