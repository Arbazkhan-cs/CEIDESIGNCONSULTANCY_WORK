import json
import requests
import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=1"
}

def get_data(url, headers):
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    return json_data

start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)
all_date = []

while start_date < end_date:
    all_date.append(start_date.strftime("%Y-%m-%d"))
    start_date += timedelta(days=1)

json_arr = []
url = "https://vegetablemarketprice.com/api/dataapi/market/delhi/daywisedata?date="
for date in tqdm(all_date):
    data = get_data(url + date, headers)
    for item in data["data"]:
        veg_name = str(item["vegetablename"])
        price = str(item["price"])
        retail_price = str(item["retailprice"])
        unit = str(item["units"])
        mall_price = str(item["shopingmallprice"])
        vege_image = str(item["table"]["table_image_url"])

        newJs = {
            "date": date,
            "state_name": "Delhi",
            "veg_name": veg_name,
            "price": price,
            "retail_price": retail_price,
            "unit": unit,
            "mall_price": mall_price,
            "vege_image": vege_image
        }

        json_arr.append(newJs)

df = pd.DataFrame(json_arr)
df.to_csv("project2_data.csv", index=True)