# TaiwanStockRevenueInspector

## Requirements
```shell
pip3 install -r requirements.txt
```
- pandas
- request-html
- openpyxl
- tabulate
- xlwt

## 使用方法
1. 將想要觀察的土票代碼寫入 [stocks.txt](https://github.com/RainBoltz/TaiwanStockRevenueInspector/blob/master/stocks.txt) 檔案內
```
3008
2912
1565
...
```
2. 進入資料夾內執行
```shell
python3 main.py
```
3. terminal會顯示最新的網頁資料，同時輸出一個[檔案](https://github.com/RainBoltz/TaiwanStockRevenueInspector/blob/master/2019-04-18.xls)

![example1image](https://github.com/RainBoltz/TaiwanStockRevenueInspector/blob/master/example1.PNG)

4. 其中輸出的[檔案](https://github.com/RainBoltz/TaiwanStockRevenueInspector/blob/master/2019-04-18.xls)，會標記近 N 天更新營收的股票

![example2image](https://github.com/RainBoltz/TaiwanStockRevenueInspector/blob/master/example2.PNG)

5. 設定 N 天的程式碼區段在 [main.py](https://github.com/RainBoltz/TaiwanStockRevenueInspector/blob/master/main.py)：
```python
look_back = 10 # 標記出N天內更新的資訊
```

