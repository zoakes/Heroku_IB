#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:40:53 2020

@author: zoakes
"""

"""
IBDash: IB Automated Trading Dashboard

Program Version 1.0.1
By: Zach Oakes


Revision Notes:
1.0.0 (03/05/2020) - Initial Structure Build 
1.0.1 (03/05/2020) - Refactored


"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from assets import aggregate, individual


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#colors = {"background": "#ffffff", "background_div": "black", 'text': '#050099'}
colors = {
    'background': '#111111',
    'text': '#ffffff',
    'primary':'black',
}
app.config['suppress_callback_exceptions']= True

###############################################################################  -- TABS

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('IBMonitor', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.H6('An Automated Trade Monitoring Dashboard', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.H6('Developed by Z.Oakes', style={
           'textAlign': 'center',
            'color': colors['text']
        }),


      dcc.Tabs(id="tabs", className="row", style={'backgroundColor':'dimgray',"margin": "2% 3%","height":"20","verticalAlign":"middle"}, value='dem_tab', children=[
        dcc.Tab(label='Aggregate', value='dem_tab'),
        dcc.Tab(label='Individual', value='med_tab')
        # dcc.Tab(label='Re-admissions', value='readmit_tab')
    ]),
    html.Div(id='tabs-content')
])
    
#Select Which Tab!! (Maybe make this a Selector -- for Agg, All, or Individual Positions)
#Would require a loop in dcc.Tabs (for i in self.OPLs:)
from dash.dependencies import Input, Output
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'dem_tab':
        return aggregate.tab_1_layout
    elif tab == 'med_tab':
        return individual.tab_2_layout
    
    

    
if __name__ == '__main__':
    app.run_server()
