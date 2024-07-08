import requests
import json
import pandas as pd
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=1"
}

url = "https://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date=2024-07-07"

data = requests.get(url, headers=header)
js_data = json.loads(data.text)

js_array = []

for item in js_data["data"]:
    print(item)
    veg_name = str(item["vegetablename"])
    price = str(item["price"])
    retail_price = str(item["retailprice"])
    unit = str(item["units"])
    mall_price = str(item["shopingmallprice"])

    newJs = {
        "data": str(data),
        "veg_name": veg_name,
        "price": price,
        "retail_price": retail_price,
        "unit": unit,
        "mall_price": mall_price
    }

    js_array.append(newJs)

df = pd.DataFrame(js_array)
df.to_csv("data.csv", index=True)