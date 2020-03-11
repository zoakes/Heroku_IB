#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:27:03 2020

@author: zoakes
"""

## GRAPHS -- using plotly 
import plotly.graph_objs as go

fig = go.Figure(go.Indicator(
        mode= "number+delta",
        value=400,
        number={'prefix':"$"},
        delta={'position': "top", 
               'reference':320}, #PAST VALUE !
        domain= {'x': [0,1], 'y' : [0,1]}
        ))
fig.update_layout(paper_bgcolor='black')

fig.show()