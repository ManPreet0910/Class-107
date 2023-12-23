import pandas as pd
import csv
from plotly import graph_objs as go

df = pd.read_csv("data.csv")

student_df = df.loc[df["student_id"] == "TRL_xsl"]

fig = go.Figure(go.Bar(x = student_df.groupby("level")["attempt"].mean(), 
                       y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation = "h"
                       ))

fig.show()