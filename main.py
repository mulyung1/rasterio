'''
this app looks at the basic manipulations of geospatial raster data with rasterio
'''

import dash
from dash import Dash, dcc, html, callback, Output, Input, State
import dash_bootstrap_components as dbc
appstyle='https://codepen.io/chriddyp/pen/bWLwgP.css'
FA621 = 'https://use.fontawesome.com/releases/v6.2.1/css/all.css'
APP_TITLE='Raster Geo-Analysis'

app=Dash(
    __name__,
    external_stylesheets=[appstyle, dbc.themes.VAPOR, FA621],
    #meta_tags ensure content is scales correctly in different screen sizes
    meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1'}],
    title=APP_TITLE,
    use_pages=True
)

#for production to a a gunicor/ another WSGI server
server=app.server

#dbc Row and col component to create the sidebar header
#i.e the title, toggle, 
navbarHeader=dbc.Row(
    [
        dbc.Col(html.H3('Geo-Spatial Analysis', className='display-3')),
        dbc.Col(
            [
                html.Button(
                    #button used as toggle via Bootstrap navbar-toggle class
                    html.Span(className='navbar-toggler-icon'),
                    className='navbar-toggler',
                    id='sidebar_toggle',
                    style={'fontSize':20}
                ),
                html.Button(
                    #button used as toggle via Bootstrap navbar-toggle class
                    html.Span(className='navbar-toggler-icon'),
                    className='navbar-toggler',
                    id='topbar_toggle',
                    style={'fontSize':20}
                ),
            ],
            width='auto',
            align='center'
        )

    ]
)

navbar=html.Div(
    [
        navbarHeader,
        html.Div(
            [
                html.Hr(),
                html.P('A Geo-spatial analytical dashboard based on Python; Developed by MGC SoftWare Solutions', className='lead', style={'fontSize':15})
                
            ],
            id='blurb'
        ),
        #collapse component - animates hiding/revealing of links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.I(
                                className='fa-solid fa-magnifying-glass-chart'
                            ), 
                            'Spatial Analysis' #text beside icon
                        ],
                        href='/', 
                        active='exact', 
                        style={'fontSize':15}),
                ],
                vertical=True,
                pills=True,
            ),
            id='collapse'
        )
    ],
    id='navbar'
)

content=html.Div(dash.page_container, id='page_content')

#define app layout
app.layout=dcc.Loading(
    id='loading_page',
    type='dot',
    overlay_style={'visibility':'visible'},
    color='blue',
    children=[
        dbc.Row(
            [
                dcc.Location(id='url'),
                navbar,
                content,
            ]
        )
    ]
)

#sidebar collapsing toggle callback
@callback(
    Output('navbar','className'),
    Input('sidebar_toggle','n_clicks'),
    [State('navbar','className')]
)
def toggle_className(n, className):
    if n and className=='':
        return 'collapsed'
    return ''

#topbar_toggle activity
@callback(
    Output('collapse', 'is_open'),
    Input('topbar_toggle', 'n_clicks'),
    [State('collapse', 'is_open')]
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#run the app
if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=1111)