from dash import Dash, html
import dash_bootstrap_components as dbc
from src.components.layout import create_layout


def main() -> None:
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Medal dashbord"
    app.layout = create_layout(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()