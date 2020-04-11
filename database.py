token = "eyJhbGciOiJFUzI1NksiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiIxM0JKUVhhZHU0Yk1lQkg5QmpYTlg5YmE5dFdYTDh6SkhFIiwiaXNzdWVyIjoiZ2VuZXJpYy1iaXRhdXRoIn0.SCtvSGxGaytOa1V1Q3ZJSGhtdXBQMkdCMWxVRWdYU1orZDc1QUJBY0llQ3pEME9iSjdXQ0dLaVhua2c5NmFDNFIreWNESWdFcTFnVWFvS25qSDJqQll3PQ"

import json
import requests

query = {
  "q": {
    "find": { "out.s2": "veritable.tech", "blk.i": { "$gt": 600000 } },
    "sort": { "blk.i": 1 },
    "project": { "tx.h": 1, "out.s3": 1 }
  }
}
headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'token': token }
body = json.dumps(query)
r = requests.post(f'https://txo.bitbus.network/block',
                  headers=headers,
                  data=body,
                  stream=True)
for line in r.iter_lines():
    print(line)
