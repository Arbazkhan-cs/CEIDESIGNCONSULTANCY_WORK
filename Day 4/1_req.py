import requests
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
print(data.text)
