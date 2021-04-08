import pandas as pd 
import plotly.express as px 
from collections import Counter
data1 = pd.read_csv('coviddata.csv') 
fig = px.scatter(data1,x='date',y='cases',color='country')
fig.show()