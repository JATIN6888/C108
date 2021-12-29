import csv 
import plotly.figure_factory as pf
import pandas as pd

df=pd.read_csv("data.csv")
fig=pf.create_distplot([df["Avg Rating"].to_list()],[",Avg Rating"])
fig.show()