import requests

API_KEY = 'YOUR_API_KEY'
origin = '東京駅'
destination = '成田空港'

url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&departure_time=now&key={API_KEY}"

response = requests.get(url)
data = response.json()

# 必要な情報を抽出
distance = data['rows'][0]['elements'][0]['distance']['text']
duration = data['rows'][0]['elements'][0]['duration_in_traffic']['text']

print(f"距離: {distance}")
print(f"所要時間（交通状況を考慮）: {duration}")