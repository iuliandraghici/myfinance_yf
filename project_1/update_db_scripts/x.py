import yfinance

# get the data in a dataframe object
tsla = yfinance.Ticker("AAPL")
dataframe = tsla.history("max")
dataframe.reset_index()

# draw the plot/figure/diagram
from plotly import graph_objects
scatter = graph_objects.Scatter(x=dataframe.index, y=dataframe["Close"])
diagram = graph_objects.Figure([scatter])
diagram.show()

# dataframe2 = tsla.financials
# print(dataframe2)
# dataframe2.reset_index()
# scatter2 = graph_objects.Scatter(x=dataframe2.index, y=dataframe2["2021-12-31"])
# diagram2 = graph_objects.Figure([scatter2])
# diagram2.show()
