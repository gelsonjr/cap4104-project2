from pprint import pprint
import requests
import json

## Fetching data from World Bank API
# year_2021 = 2021
# api_url = f"https://api.worldbank.org/v2/en/country/all/indicator/SP.POP.TOTL?format=json&per_page=2&date={year_2021}"
# response = requests.get(api_url)
# data = response.json()

# with open("tests/jason60.json") as f:
#    data = json.load(f)

# json_data = json.dumps(data[1][49:])
#data = data[1][49:]

# data = str(data[1][49:])[1:-1] #Maybe?


url = 'tests/data2021_api.json'
with open(url, "r") as jf:
    json_file = json.load(jf)

data_2021 = {}

for index in range(50, len(json_file[1])):
    data_2021.update(
        {json_file[1][index]['country']['value']: json_file[1][index]['value']}
    )
    # data_2021.append({
    #     json_file[1][index]['country']['value']: json_file[1][index]['value']
    #     # "Country": json_file[1][index]['country']['value'],
    #     # "Population": json_file[1][index]['value'],
    #     # "Year": json_file[1][index]['date']
    # })


print(data_2021)

# print(json_file[1][1]['country']['id'])
# print(json_file[1][1]['country']['value'])
# print(json_file[1][1]['value'])
# print(json_file[1][1]['date'])

# for i in json_file[1][1]['country']:
#     print(i[0])
# print(i['value'])