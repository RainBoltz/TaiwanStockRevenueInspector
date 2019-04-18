import pandas as pd
import requests_html as req
import numpy as np
import sys
from datetime import datetime, timedelta
from tabulate import tabulate
from pandas_excel_styler import DataFrameExcelStyler

# 確認選擇之股票代碼
with open('stocks.txt','r') as f:
    stocks = f.readlines()
stocks = [x.strip() for x in stocks]

# 獲取網頁資料
session = req.HTMLSession()
result = session.get(r'http://invest.wessiorfinance.com/new_revenue.html')
result.encoding="utf-8"

# 讀入pandas表格
try:
    data = pd.read_html(result.text)[0]
except Exception as e:
    print("網頁讀取失敗！")
    print(str(e))
    sys.exit(0)

# 取得選定股票
output_df = pd.DataFrame()
for stock in stocks:
    if int(stock) in data['股票代號']:
        output_df = output_df.append(data[data['股票代號']==int(stock)])
output_df.reset_index(drop=True, inplace=True)
print(tabulate(output_df, headers='keys'))

# 提示今日最新
df = DataFrameExcelStyler(output_df)
red_font_style = {"font": {"color": "red"}}
cell_styles = np.empty(output_df.shape, dtype='object')
cell_styles.fill(None)

look_back = 10 # 標記出N天內更新的資訊
today = datetime.now().strftime("%Y-%m-%d")
base_dt = datetime.now() - timedelta(days=look_back)
for i in range(len(output_df)):
    if datetime.strptime(output_df['公布日期'].iloc[i], "%Y-%m-%d") >= base_dt:
        for j in range(len(df.columns)):
            cell_styles[i, j] = red_font_style
df.to_excel('%s.xls'%today, cell_styles=cell_styles)










    
    