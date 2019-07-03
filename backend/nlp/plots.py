# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:37:23 2019

@author: asuer
pltly api DgWPnl5qUOsmsiYMefrk
user : ahmetsuerdem

"""

# 1. Plotly scatter plots
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

#dfxx

df =pd.read_json('ai_cntries.json')

#1. barplots
sr = df['source'].value_counts()
sr = pd.DataFrame(sr[(sr >= 20)])
con = pd.DataFrame(df['country'].value_counts())
yr = pd.DataFrame(df['year'].value_counts())

sr = sr.sort_values(by='source', ascending=True)
data  = go.Data([
            go.Bar(
              y = sr.index,
              x = sr.source,
              orientation='h'
        )])
layout = go.Layout(
        title = "Number of AI articles by newspapers"
)
fig  = go.Figure(data=data, layout=layout)
py.plot(fig)

#2. stacked barplots
temp1 = pd.crosstab(df['source']  ,df['year'])
temp1.reset_index(level=0, inplace=True)


trace1 = go.Bar(
    x=temp1['source'],
    y=temp1[2016],
    name='2016'
)
trace2 = go.Bar(
    x=temp1['source'],
    y=temp1[2017],
    name='2017'
)

trace3 = go.Bar(
    x=temp1['source'],
    y=temp1[2018],
    name='2017'
)

trace4 = go.Bar(
    x=temp1['source'],
    y=temp1[2019],
    name='2017'
)

layout = go.Layout(
    barmode='relative')


data =[trace1, trace2, trace3, trace4]
fig=dict(data =data, layout=layout )
py.plot(fig)


#3. DATE
dt =pd.DataFrame(df['date'].value_counts())
dt.reset_index(level=0, inplace=True)
dt = dt.sort_values(by='index', ascending=True)
dt.columns


dt['index']=pd.to_datetime(dt['index'], format='%Y')



data = [go.Scatter(
                x=dt['index'],
                y=dt.date,
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)]

layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1yr',
                     step='year',
                     stepmode='backward'),
                dict(count=5,
                     label='5yr',
                     step='year',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
py.plot(fig)


