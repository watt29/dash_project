from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello, Dash on Heroku!"),
    html.P("This is a simple Dash app deployed on Heroku.")
])

if __name__ == "__main__":
    app.run_server(debug=False)
