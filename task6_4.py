import requests
import urllib
import pandas as pd
import pprint
import numpy as np

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
APP_ID = '1082837595031535108'

#必須パラメーター入力
params = {
    'format':'json',
    'genreId':'566483',
    'applicationId':APP_ID
}

res = requests.get(REQUEST_URL,params)
result = res.json()

item_key = ['itemName','rank','itemPrice','reviewAverage']
item_list = []
for i in range(0, len(result['Items'])):
    tmp_item = {}
    item = result['Items'][i]['Item']
    for key, value in item.items():
        if key in item_key:
            tmp_item[key] = value
    item_list.append(tmp_item)

items_df = pd.DataFrame(item_list)
items_df = items_df.reindex(columns=['itemName','rank','itemPrice','reviewAverage'])
items_df.columns = ['商品名','ランキング','価格','平均評価']
items_df.index = np.arange(1,31)
items_df.to_csv('./item_3.csv')