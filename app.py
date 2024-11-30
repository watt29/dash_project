import dash
from dash import dash_table
import pandas as pd
from dash import html

# ข้อมูลที่ได้จากตัวอย่าง
data = [
    {"date": "2 มีนาคม 2564", "order_number": "เล่มที่ 13 เลขที่ 9", "product": "น้ำมันเบนซิน", "amount_liters": 5.9, "total_cost": 200.00, "remaining_budget": 73_415.00, "equipment": "เครื่องตัดหญ้าศูนย์พัฒนาเด็กเล็กฯ"},
    {"date": "2 มีนาคม 2564", "order_number": "เล่มที่ 13 เลขที่ 8", "product": "น้ำมันเบนซิน", "amount_liters": 7.43, "total_cost": 250.00, "remaining_budget": 73_215.00, "equipment": "เครื่องตัดหญ้า รร.เทศบาล 6"},
    {"date": "9 มีนาคม 2564", "order_number": "เล่มที่ 14 เลขที่ 20", "product": "น้ำมันดีเซลB7", "amount_liters": 82.24, "total_cost": 2_250.00, "remaining_budget": 72_965.00, "equipment": "รถสองแถว 40-0163 สุพรรณบุรี"},
    {"date": "16 มีนาคม 2564", "order_number": "เล่มที่ 15 เลขที่ 27", "product": "น้ำมันดีเซลB7", "amount_liters": 58.48, "total_cost": 1_600.00, "remaining_budget": 70_715.00, "equipment": "รถกระบะ กบ 5274 สุพรรณบุรี"},
    {"date": "29 มีนาคม 2564", "order_number": "เล่มที่ 17 เลขที่ 37", "product": "น้ำมันเบนซิน", "amount_liters": 7.41, "total_cost": 250.00, "remaining_budget": 69_115.00, "equipment": "เครื่องตัดหญ้าศูนย์พัฒนาเด็กเล็กฯ"},
    {"date": "29 มีนาคม 2564", "order_number": "เล่มที่ 17 เลขที่ 43", "product": "น้ำมันดีเซล87", "amount_liters": 64.49, "total_cost": 1_700.00, "remaining_budget": 68_865.00, "equipment": "รถกระบะ กบ 5274 สุพรรณบุรี"}
]

# สร้าง DataFrame จากข้อมูล
df = pd.DataFrame(data)

# สร้างแอพ Dash
app = dash.Dash(__name__)

# Layout ของแอพ
app.layout = html.Div([
    # ข้อความบนตาราง
    html.Div([
        html.H3("รายงานขอซื้อที่ผู้สั่งซื้อให้ความเห็นชอบ เลขที่ 1/2564"),
        html.P("วงเงินที่ผู้สั่งซื้อให้ความเห็นชอบ: 100,000 บาท")
    ], style={
        'textAlign': 'center',  # จัดข้อความให้ชิดกลาง
        'marginBottom': '20px',  # ระยะห่างจากด้านล่าง
    }),

    # ตารางข้อมูล
    dash_table.DataTable(
        id='oil-purchase-table',
        columns=[
            {'name': 'วันที่', 'id': 'date'},
            {'name': 'ใบสั่งซื้อ/ใบเสร็จรับเงิน', 'id': 'order_number'},
            {'name': 'ประเภทน้ำมัน', 'id': 'product'},
            {'name': 'ปริมาณ (ลิตร)', 'id': 'amount_liters'},
            {'name': 'วงเงิน (บาท)', 'id': 'total_cost'},
            {'name': 'งบประมาณคงเหลือ (บาท)', 'id': 'remaining_budget'},
            {'name': 'ประเภทของครุภัณฑ์', 'id': 'equipment'},
        ],
        data=df.to_dict('records'),
        style_table={'height': '400px', 'overflowY': 'auto'},
        style_cell={'textAlign': 'center'},
        style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'},
    )
])

# รันแอพ
if __name__ == '__main__':
    app.run_server(debug=True)
