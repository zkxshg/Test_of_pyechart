from pyecharts import Kline
import pandas as pd
import tushare as ts
import time

#大盤指數
# 設定期限
df7 = ts.get_hist_data('600848', start='2017-01-05', end='2017-02-05')
# 一次性获取全部日k线数据
# df7 = ts.get_hist_data('600848')
df7.to_csv('data.csv')

# 讀取指數
date = pd.read_csv('data.csv', usecols=[0]).values
close = pd.read_csv('data.csv', usecols=[1, 3, 2, 4]).values

# 繪製K線圖
kline = Kline("k線圖案例")
kline.add("大盤", date, close)
kline.render()

