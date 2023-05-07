from dash import html, dcc
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "24rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


def get_structure():
    return html.Div(
        children=[
            dcc.Location(id="url"),
            dbc.Row(
                [
                    dbc.Col(),
                    dbc.Col(
                        html.H1("Track the Circle Line"),
                        width=9,
                        style={"margin-left": "7px", "margin-top": "7px"},
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(sidebar),
                    dbc.Col(
                        html.Div(id="page-content", style=CONTENT_STYLE), width=9
                    ),  # dcc.Graph(id = 'graph1', figure = fig1), width = 9, style = {'margin-left':'15px', 'margin-top':'7px', 'margin-right':'15px'}
                ]
            ),
        ]
    )


sidebar = html.Div(
    [
        html.H2("Pages"),
        html.Hr(),
        html.P("Choose the functionality:", className="lead"),
        # dbc.Nav(
        #     [
        #         dcc.Dropdown(id="one"),
        #         html.Br(),
        #         dcc.Dropdown(id="two"),
        #         html.Br(),
        #         dcc.Dropdown(id="three"),
        #     ],
        #     vertical=True,
        #     pills=True,
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Tube Stations Map", href="/", active="exact"),
                dbc.NavLink("Shepherd's Bush Arrivals", href="/page-1", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
