from dash import Dash, html, dash_table
import pandas as pd
import sqlite3

# สร้างแอป Dash
app = Dash(__name__)

# เชื่อมต่อกับฐานข้อมูล SQLite
conn = sqlite3.connect('vehicles.db')
query = "SELECT * FROM vehicles"

# ดึงข้อมูลจากฐานข้อมูลและแปลงเป็น DataFrame
df = pd.read_sql(query, conn)

# ปิดการเชื่อมต่อฐานข้อมูล
conn.close()

# สร้างเลย์เอาต์ของแอปพลิเคชัน Dash
app.layout = html.Div([
    html.H1("ข้อมูลยานพาหนะจากฐานข้อมูล"),
    dash_table.DataTable(
        id='vehicle-table',
        columns=[
            {'name': col, 'id': col} for col in df.columns
        ],
        data=df.to_dict('records'),
        style_table={'height': '400px', 'overflowY': 'auto'},  # สำหรับให้แสดงตารางในขนาดที่พอเหมาะ
    ),
])

# รันแอปพลิเคชัน
if __name__ == '__main__':
    app.run_server(debug=True)
