import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot


# df = pd.read_csv('2014_World_Power_Consumption')

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

# data = dict(
#     z = df['Power Consumption KWH'],
#     locations = df['Country'],
#     colorscale = scl,
#     autocolorscale = False,
#     type='choropleth',
#     locationmode = 'country names',
#     colorbar={'title': 'Power Consumption in KWH'}
# )
#
# layout = dict(
#     title = '2014 World Power Consumption',
#     geo = dict(
#         showframe = False,
#         projection = {'type':'mercator'})
# )

#choromap = go.Figure([data],layout)

#plot(choromap)

df2 = pd.read_csv('2012_Election_Data')

a= []
for i in range(0,51):
    if not i == 8:
        a.append(i)
df2.iloc[a][['Voting-Age Population (VAP)','State Abv']]

data2 = dict(
    z = df2['Voting-Age Population (VAP)'],
    locations = df2['State Abv'].iloc[range(0,9),range(9,51)],
    colorscale = scl,
    autocolorscale = False,
    type='choropleth',
    colorbar={'title': 'Voting-Age Population'},
    text = df2['State']
)

layout2 = dict(
    title = '2012 Election Data',
    geo=dict(scope='usa',
             showlakes=True,
             lakecolor='rgb(85,173,240)')
)

choromap2 = go.Figure(data=[data2], layout=layout2)

plot(choromap2,validate=False)

#
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 51 entries, 0 to 50
# Data columns (total 17 columns):
# Year                                51 non-null int64
# ICPSR State Code                    51 non-null int64
# Alphanumeric State Code             51 non-null int64
# State                               51 non-null object
# VEP Total Ballots Counted           41 non-null object
# VEP Highest Office                  51 non-null object
# VAP Highest Office                  51 non-null object
# Total Ballots Counted               41 non-null object
# Highest Office                      51 non-null object
# Voting-Eligible Population (VEP)    51 non-null object
# Voting-Age Population (VAP)         51 non-null float64
# % Non-citizen                       51 non-null object
# Prison                              51 non-null object
# Probation                           51 non-null object
# Parole                              51 non-null object
# Total Ineligible Felon              51 non-null object
# State Abv                           51 non-null object
# dtypes: float64(1), int64(3), object(13)
# memory usage: 6.9+ KB
