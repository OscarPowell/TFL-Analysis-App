from dash import Dash
import dash_bootstrap_components as dbc
from structure import get_structure
from callbacks import callbacks
import pickle
from settings import SETTINGS

app = Dash(
    __name__,
    title="tfl-app",
    external_stylesheets=[
        dbc.themes.MINTY,
    ],
)

# # Load from flat file
file = open(SETTINGS["RESPONSE_PATH"], "rb")
response = pickle.load(file)
file.close()

server = app.server

app.layout = get_structure()

callbacks(app, response)

if __name__ == "__main__":
    app.run_server(debug=True)
