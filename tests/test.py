from pprint import pprint
import requests
import json

## Fetching data from World Bank API
# year_2021 = 2021
# api_url = f"https://api.worldbank.org/v2/en/country/all/indicator/SP.POP.TOTL?format=json&per_page=2&date={year_2021}"
# response = requests.get(api_url)
# data = response.json()

with open("tests/jason60.json") as f:
   data = json.load(f)

json_data = json.dumps(data[1][49:])
#data = data[1][49:]

# data = str(data[1][49:])[1:-1] #Maybe?

#print(dataTrimmed)
print(json_data)
#pprint(data[0][0])
#print(text1)
#print("Hello")