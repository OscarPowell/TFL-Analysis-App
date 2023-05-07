from dash import Dash
import dash_bootstrap_components as dbc
from app.structure import get_structure
from app.callbacks import callbacks

app = Dash(__name__, title="tfl-app", external_stylesheets=[dbc.themes.MINTY])

server = app.server

app.layout = get_structure()

callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
