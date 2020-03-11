#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:52:57 2020

@author: zoakes
"""
import dash
import dash_html_components as html
import dash_core_components as dcc

import plotly.graph_objs as go

big_card = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=120,
        #title='Open PNL',
        number={'prefix':'$'},
        delta={'position': 'top', 
               'reference':110.8}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
big_card.update_layout(title_text='Position A',paper_bgcolor='black')

real = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=120,
        #title='Open PNL',
        number={'prefix':'$'},
        delta={'position': 'top', 
               'reference':100.06}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
real.update_layout(title_text='Position B',paper_bgcolor='black')


## Row 2 

posc = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=120,
        #title='Open PNL',
        number={'prefix':'$'},
        delta={'position': 'top', 
               'reference':155.10}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
posc.update_layout(title_text='Position C',paper_bgcolor='black')

posd = go.Figure(go.Indicator(
        mode= 'number+delta',
        value=100,
        #title='Open PNL',
        number={'prefix':'$'},
        delta={'position': 'top', 
               'reference':80.5}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
posd.update_layout(title_text='Position D',paper_bgcolor='black')

tab_2_layout = html.Div([
            #Row 1 -- 
            html.Div([
                html.Div([
                    html.H6('Open Position A',style={'textAlign': 'center'}),
                    dcc.Graph(
                        id='med-graph-1',
                        figure=big_card,
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Open Position B',style={'textAlign': 'center'}),
                    dcc.Graph(
                        id='med-graph-2',
                        figure=real,
                    )
                ], className="six columns"),
            ], className="row", style={"margin": "1% 3%"}),

            #Row 2 !!
            html.Div([
                html.Div([
                    html.H6('Open Position C',style={'textAlign': 'center'}),
                    dcc.Graph(
                        id='med-graph-1',
                        figure=posc,
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Open Position D',style={'textAlign': 'center'}),
                    dcc.Graph(
                        id='med-graph-2',
                        figure=posd,
                    )
                ], className="six columns"),

            ], className="row", style={"margin": "1% 3%"})
    ])