from pydantic import BaseModel, Field

#TODO create model for adding a stock & a model for getting a stock
# if another domain in your project, create different models for POST & GET
class StockModel(BaseModel):
    ticker: str = Field(description="The ticker ID of the stock, for example Tesla has TSLA")
    company: str = Field(default="", description="The full company name, leave empty for POST")
    field: str = Field(default="")
    long_summary: str = Field(default="", description="The business summary of the company")
    exchange: str = Field(default="", description="The name of the exchange where the company is listed")

    class Config:
        orm_mode = True
