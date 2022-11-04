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

#print(dataTrimmed)
# print(json_data)
#pprint(data[0][0])
#print(text1)
#print("Hello")

url = 'tests/data2019_2021.json'
with open(url, "r") as jf:
    json_file = json.load(jf)

data_2021 = []

# for country_code, name, population, year in json_file.items():
#     print

#print(json_file[1])
for index in range(0, len(json_file[1]) - 2, 3):
    data_2021.append({
        "Country": json_file[1][index]['country']['value'],
        "Code": json_file[1][index]['country']['id'],
        "Population in 2019": json_file[1][index + 2]['value'],
        "Population in 2020": json_file[1][index + 1]['value'],
        "Population in 2021": json_file[1][index]['value'],
        #"Year": json_file[1][index]['date'],
    })
    print("index: ", index)

print(data_2021[49:])

# print(json_file[1][1]['country']['id'])
# print(json_file[1][1]['country']['value'])
# print(json_file[1][1]['value'])
# print(json_file[1][1]['date'])

# for i in json_file[1][1]['country']:
#     print(i[0])
# print(i['value'])