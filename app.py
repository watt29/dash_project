import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# สร้างแอปพลิเคชัน Dash
app = dash.Dash(__name__)

# ข้อมูลตัวอย่าง
df = px.data.gapminder()

# Layout ของแอปพลิเคชัน
app.layout = html.Div([
    html.H1("ตัวอย่าง Dashboard ด้วย Dash", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='dropdown-country',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='Thailand',
        placeholder='เลือกประเทศ',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='line-chart'),
    html.Div(id='output-div', style={'textAlign': 'center', 'marginTop': '20px'})
])

# Callback เพื่ออัปเดตกราฟและข้อมูล
@app.callback(
    [Output('line-chart', 'figure'),
     Output('output-div', 'children')],
    [Input('dropdown-country', 'value')]
)
def update_chart(selected_country):
    if selected_country:
        filtered_df = df[df['country'] == selected_country]
        fig = px.line(
            filtered_df,
            x='year',
            y='lifeExp',
            title=f'Life Expectancy ใน {selected_country}',
            labels={'lifeExp': 'อายุเฉลี่ย (ปี)', 'year': 'ปี'}
        )
        return fig, f"คุณเลือกประเทศ: {selected_country}"
    return {}, "กรุณาเลือกประเทศจาก Dropdown"

# รันเซิร์ฟเวอร์
if __name__ == '__main__':
    app.run_server(debug=True)
