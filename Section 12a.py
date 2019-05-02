import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

# init_notebook_mode(connected=True)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]
df = pd.read_csv('2011_US_AGRI_Exports')

data = dict(
    type='choropleth',
    locations=df['code'],
    locationmode='USA-states',
    colorscale=scl,
    autocolorscale=False,
    text=df['text'],
    z=df['total exports'],
    colorbar={'title': 'colorbar title goes here'})

layout = dict(
    title='2011 US Agriculture Exports by State',
    geo=dict(scope='usa',
             showlakes=True,
             lakecolor='rgb(85,173,240)')
)
choromap = go.Figure(data=[data], layout=layout)

plot(choromap)

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 50 entries, 0 to 49
# Data columns (total 18 columns):
# code             50 non-null object
# state            50 non-null object
# category         50 non-null object
# total exports    50 non-null float64
# beef             50 non-null float64
# pork             50 non-null float64
# poultry          50 non-null float64
# dairy            50 non-null float64
# fruits fresh     50 non-null float64
# fruits proc      50 non-null float64
# total fruits     50 non-null float64
# veggies fresh    50 non-null float64
# veggies proc     50 non-null float64
# total veggies    50 non-null float64
# corn             50 non-null float64
# wheat            50 non-null float64
# cotton           50 non-null float64
# text             50 non-null object
# dtypes: float64(14), object(4)
# memory usage: 7.1+ KB
