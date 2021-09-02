import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("MarksVsPresentes.csv")
data = df["Marks In Percentage"].tolist()
data2 = df["Days Present"].tolist()
fig = px.scatter(x=data2, y=data)
fig.show()


correlation = np.corrcoef(data2, data)
print("Correlation between Marks in percentage and Days present :-  \n--->",
      correlation[0, 1])
