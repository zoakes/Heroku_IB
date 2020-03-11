#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:52:42 2020

@author: zoakes
"""
import dash
import dash_html_components as html
import dash_core_components as dcc

## GRAPHS -- using plotly 
import plotly.graph_objs as go

big_card = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=403,
        #title='Open PNL',
        number={'prefix':'$'},
        delta={'position': 'top', 
               'reference':350.8}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
big_card.update_layout(title_text='Closed PNL',paper_bgcolor='black')

real = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=122.5,
        #title='Open PNL',
        number={'prefix':'$'},
        delta={'position': 'top', 
               'reference':132.12}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
real.update_layout(title_text='Open PNL',paper_bgcolor='black')

#############

winloss = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=1.1,
        #number={'prefix':''},
        delta={'position': 'top', 
               'reference':1.06}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
winloss.update_layout(title_text='Win / Loss',paper_bgcolor='black')

##STACKED BAR 

animals=['wins','losses']

sb = go.Figure(data=[
    go.Bar(name='Current', x=animals, y=[2, 0]),
    go.Bar(name='Max', x=animals, y=[12, 4])
])
# Change the bar mode
sb.update_layout(title_text='Consecutive Trades',barmode='stack',paper_bgcolor='black',plot_bgcolor='black')
#sb.show()


## PIE CHART

labels = ['Win','Loss']
values = [72,40]

pie = go.Figure(data=[go.Pie(labels=labels, values=values)])
#pie.update_traces() #For colors
pie.update_layout(title_text='Win %',paper_bgcolor='black')
#fig.show()

## SUBPLOT -- SR RET VAR 

import pandas as pd
import pandas_datareader as pdr
import random


#Random sampling for Mu, Sig, SR
sig = [random.uniform(1,5) for i in range(100)]
mu = [random.uniform(4,10) for i in range(100)]
SR = [(m/s) for m,s in zip(mu,sig)]
SRA = [((m/s)*12)**1/2 for m,s in zip(mu,sig)]



df = pd.DataFrame({'SR':SRA,'MU':mu,'Sigma':sig})
df.rolling(window=20).mean().fillna(0)


#df = pdr.DataReader('AMD','yahoo',2019).reset_index()

#df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

SR = go.Figure()
SR.add_trace(go.Scatter(x=df.index, y=df['MU'], name="Mu",
                         line_color='#1f77b4'))

SR.add_trace(go.Scatter(x=df.index, y=df['Sigma'], name="Sigma",
                         line_color='firebrick'))

SR.add_trace(go.Scatter(x=df.index, y=df['SR'], name="SR",
                         line_color='dimgray'))

SR.update_layout(title_text='Sharpe Ratio',
                  xaxis_rangeslider_visible=True,
                  paper_bgcolor='black',
                  plot_bgcolor='black')


SR.update_xaxes(showline=True, linewidth=1, linecolor='dimgray', gridcolor='dimgray',mirror=True)
SR.update_yaxes(showline=True, linewidth=1, linecolor='dimgray', gridcolor='dimgray',mirror=True)




tab_1_layout = html.Div([
            # html.H3('Patient Demographics'),

                html.Div([
                    html.Div([
                        html.H6('Realized', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-1',
                            figure=big_card
                        )
                    ], className="four columns"),

                    html.Div([
                        html.H6('Unrealized', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-2',
                            figure=real
                        )
                    ], className="four columns"),

                    html.Div([
                        html.H6('Win : Loss', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-3',
                            figure=winloss
                        )
                    ], className="four columns")

                ], className="row", style={"margin": "1% 3%"}),

                html.Div([
                    html.Div([
                        html.H6('Efficiency', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-4',
                            figure=pie
                        )
                        ], className="six columns"),

                    html.Div([
                        html.H6('Consecutive', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-5',
                            figure=sb,
                        )
                    ], className="six columns"),
                ], className="row", style={"margin": "1% 3%"}),

                html.Div([
                    html.Div([
                        html.H6('Performance', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-6',
                            figure=SR
                        )
                    ])
                ], className="row", style={"margin": "1% 3%"})

            ]
        )