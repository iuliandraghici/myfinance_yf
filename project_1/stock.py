
class Stock:
    def __init__(self, ticker: str, company_name: str, field: str, amount: float = 0):
        self.ticker = ticker
        self.company_name = company_name
        self.field = field
        self.amount = amount

    def to_json(self) -> dict:
        return {
            "ticker": self.ticker,
            "company": self.company_name,
            "field": self.field,
            "amount": self.amount,
        }
