from dash import Input, Output, html
from page_content import get_tube_map_content, get_arrivals
from settings import SETTINGS


def callbacks(app, response):
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        paths = SETTINGS["PAGE_PATHS"]
        if pathname in paths["map"]:
            return get_tube_map_content()
        elif pathname in paths["arrivals"]:
            return get_arrivals(response)
        # If the user tries to reach a different page, return a 404 message
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )
