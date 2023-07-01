import pandas as pd

csv_kwargs = {"sep":";", }

a = pd.read_csv("01_numpy.csv", **csv_kwargs)

empty = {}

b = pd.read_csv("01_numpy.csv", **empty)
