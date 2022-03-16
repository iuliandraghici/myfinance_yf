import yfinance
from plotly import graph_objects
from matplotlib import pyplot
import random

from models import DiagramModel


def show_simple_diagram(ticker_id: str, info: str = "Close", interval: str = "3y"):
    dataframe = __get_the_data_frame(interval, ticker_id)
    # draw the plot/figure/diagram
    scatter = graph_objects.Scatter(x=dataframe.index, y=dataframe[info])
    diagram = graph_objects.Figure([scatter])
    diagram.show()


def create_and_save_to_file(model: DiagramModel):
    dataframe = __get_the_data_frame(model.interval, model.ticker)
    figure, axis = pyplot.subplots(figsize=(16, 9))
    axis.plot(dataframe.index, dataframe[model.info])
    pyplot.savefig(f"./stock/diagram/diagram_nr_{random.randrange(1000, 9999)}")


def __get_the_data_frame(interval, ticker_id):
    tsla = yfinance.Ticker(ticker_id)
    dataframe = tsla.history(interval)
    dataframe.reset_index()
    return dataframe


