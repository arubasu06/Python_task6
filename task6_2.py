import requests
import urllib
import pandas as pd
import pprint
import numpy as np

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = ''

#必須パラメーター入力
page = 1
params = {
    'format':'json',
    'keyword':'ガンダム',
    'applicationId':APP_ID
}
res = requests.get(REQUEST_URL,params)
result = res.json()

item_key = ['itemName','itemPrice','shopName','shopUrl','reviewAverage','itemUrl']
item_list = []
for i in range(0, len(result['Items'])):
    tmp_item = {}
    item = result['Items'][i]['Item']
    for key, value in item.items():
        if key in item_key:
            tmp_item[key] = value
    item_list.append(tmp_item)

items_df = pd.DataFrame(item_list)
items_df = items_df.reindex(columns=['itemName','itemPrice','shopName','shopUrl','reviewAverage','itemUrl'])
items_df.columns = ['a','b','C','d','e','f']
items_df.index = np.arange(1,31)
items_df.to_csv('./item.csv')