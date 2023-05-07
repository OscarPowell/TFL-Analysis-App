from dash import html, dcc
import folium

def get_tube_map_content():
    content = html.Div("This is the main content")
    return content


def get_other_content():
    return html.Div("This is other Content")
