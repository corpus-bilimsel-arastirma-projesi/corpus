# -*- coding: utf-8 -*-

# 1. Plotly scatter plots
import plotly.graph_objs as go
from plotly.offline import plot
import pandas as pd

# 1. barplots

#does not work properly unless category=source
def valueCounter(category,number,dataframe):
    sr = dataframe[category].value_counts()
    sr = pd.DataFrame(sr[(sr >= number)])
# replace sr w others
    sr = sr.sort_values(by=category, ascending=True)
    data = [go.Bar(
        x=getattr(sr,category),
        y=sr.index,
        orientation='h')]
    layout = go.Layout(
        title="There is a title"
    )
    fig = go.Figure(data=data, layout=layout)
    #plot(fig, auto_open=True)
    return fig

# 2. stacked barplots
def stackedPlot(category1,category2,dataframe):
    test5 = pd.crosstab(index=dataframe[category1], columns=dataframe[category2])

    li = []
    for i in test5:
        x = test5[i].to_dict()
        li.append(x)
    x_data = []
    y_data = []
    for i in li:
        x = list(i.keys())
        y = list(i.values())
        x_data.append(x)
        y_data.append(y)

    traces = []
    for i in range(0, len(dataframe[category2].unique())):
        traces.append(go.Bar(
            x=x_data[i],
            y=y_data[i],
            name=str(test5.columns[i])
        ))

    layout = go.Layout(
        barmode='stack')

    fig = go.Figure(data=traces, layout=layout)
    #plot(fig)
    return fig

# 3. date with sliderand smoother
'''
from scipy import signal

dt = pd.DataFrame(df['date'].value_counts())
dt.reset_index(level=0, inplace=True)
dt = dt.sort_values(by='index', ascending=True)
dt['dat'] = pd.to_datetime(dt['index'], format='%Y')

trace1 = go.Scatter(
    x=dt['dat'],
    y=dt['date'],
    line=dict(color='#7F7F7F'),
    opacity=0.8)

trace2 = go.Scatter(
    x=dt['dat'],
    y=signal.savgol_filter(dt['date'], 75, 10),
    mode='markers',
    marker=dict(
        size=6,
        color='#C190F0',
        symbol='triangle-up'
    ),
    name='Savitzky-Golay'
)

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
            visible=True
        ),
        type='date'
    )
)

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
plot(fig)
'''

# 4. with multiple lines date

def multipleLinesGraph(category1,category2,dataframe):
    test6 = pd.crosstab(index=dataframe[category1], columns=dataframe[category2])
    test6 = test6.sort_values(by=category1, ascending=True)

    li = []
    for i in test6:
        x = test6[i].to_dict()
        li.append(x)
    x_data = []
    y_data = []
    for i in li:
        x = list(i.keys())
        y = list(i.values())
        x_data.append(x)
        y_data.append(y)

    traces = []
    for i in range(0, len(dataframe[category2].unique())):
        traces.append(go.Scatter(
            x=x_data[i],
            y=y_data[i],
            name=test6.columns[i],
            mode='lines',
            connectgaps=True
        ))

    fig = go.Figure(data=traces)
    #plot(fig)
    return fig



