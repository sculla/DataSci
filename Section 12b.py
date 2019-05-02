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
df = pd.read_csv('2014_World_GDP')


data = dict(
    type='choropleth',
    locations=df['CODE'],
    colorscale=scl,
    autocolorscale=False,
    text=df['COUNTRY'],
    z=df['GDP (BILLIONS)'],
    colorbar={'title': 'GDP in Billions USD'})

layout = dict(
    title='2014 Global GDP',
    geo=dict(
        showframe = False,
        projection = {'type':'mercator'}))
choromap = go.Figure([data],layout)

plot(choromap)

# Out[4]:
#           COUNTRY  GDP (BILLIONS) CODE
# 0     Afghanistan           21.71  AFG
# 1         Albania           13.40  ALB
# 2         Algeria          227.80  DZA
# 3  American Samoa            0.75  ASM
# 4         Andorra            4.80  AND