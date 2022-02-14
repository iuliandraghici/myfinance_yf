# this is our root file, when we execute this we will start our app
# webpage for fastapi framework https://fastapi.tiangolo.com/tutorial/,
# also https://realpython.com/fastapi-python-web-apis/

# uvicorn index:app --reload --port 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the code
# --port <port_number> -> select on which port to start

import json
from fastapi import FastAPI
from stock import Stock

app = FastAPI(
    title="Name of our app",  # TODO for homework, name your application
    # <major_version>.<minor_version>.<patch_version>
    version="0.2.0",  # increase version after finishing homework
    description="",  # TODO add a description
)


@app.get(
    "/health",
    summary="This will be visible at start",
    description="We can describe this API call",
    response_description="We can describe the response",
)
def health() -> dict:
    return {
        "status": "online",
        "engine": "on",
    }


# stocks will keep a list of Stock objects
stocks = {}


@app.post("/stocks")
def add_new_stock(stock_info: dict):
    new_stock = Stock(stock_info["ticker"], stock_info["company"], stock_info["field"])
    stocks[stock_info["ticker"]] = new_stock
    list_json = json.dumps([x.to_json() for x in stocks.values()])
    file = open("database.txt", "w")
    file.write(list_json)
    file.close()


# TODO return your domain items
# example if you want to do a tasks app return the list of tasks, and rename the url /items -> /tasks
@app.get("/stocks")
def get_stocks():
    return stocks


# TODO add a put method to edit your domain item
# TODO add a delete method to remove a domain item from the list
# these methods should also save the data into a file for persistence across server reboots


@app.delete("/stocks")
def remove_stock(ticker: str):
    stocks.pop(ticker)
    list_json = json.dumps([x.to_json() for x in stocks.values()])
    file = open("database.txt", "w")
    file.write(list_json)
    file.close()


@app.on_event("startup")
def load_list_of_items():
    file = open("database.txt")
    json_items = file.read()
    file.close()
    items = json.loads(json_items)
    # items = list of dictionaries from the file
    for one_item in items:
        new_stock = Stock(one_item["ticker"], one_item["company"], one_item["field"], one_item["amount"])
        stocks[one_item["ticker"]] = new_stock
