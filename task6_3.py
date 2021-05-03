import requests
import urllib
import pandas as pd
import pprint
import numpy as np

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
APP_ID = ''

#必須パラメーター入力
params = {
    'format':'json',
    'genreId':'566483',
    'keyword':'プラモデル',
    'applicationId':APP_ID
}

res = requests.get(REQUEST_URL,params)
result = res.json()

item_key = ['productName','salesMinPrice','salesMaxPrice','averagePrice','reviewCount','reviewAverage']
item_list = []
for i in range(0, len(result['Products'])):
    tmp_item = {}
    item = result['Products'][i]['Product']
    for key, value in item.items():
        if key in item_key:
            tmp_item[key] = value
    item_list.append(tmp_item)

items_df = pd.DataFrame(item_list)
items_df = items_df.reindex(columns=['productName','salesMinPrice','salesMaxPrice','averagePrice','reviewCount','reviewAverage'])
items_df.columns = ['商品名','最安値','最高値','平均値','レビュー数','平均評価']
items_df.index = np.arange(1,31)
items_df.to_csv('./item_2.csv')