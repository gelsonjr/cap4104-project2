import requests
import json
#import streamlit as st
import pandas as pd
import numpy as np
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

#url = 'tests/data2021_api.json'

def fetch_api_data(api_url):
    data = {}

    with open(api_url, "r") as jf:
        json_file = json.load(jf)

    for index in range(50, len(json_file[1])):
        data.update(
            {json_file[1][index]['country']['value']: json_file[1][index]['value']}
        )
        # data_2021.append({
        #     json_file[1][index]['country']['value']: json_file[1][index]['value']
        #     # "Country": json_file[1][index]['country']['value'],
        #     # "Population": json_file[1][index]['value'],
        #     # "Year": json_file[1][index]['date']
        # })
    return data

def create_dataframe(api_data):
    # dataframe = pd.DataFrame(data=api_data)
    dataframe = pd.DataFrame(
        {'Country': api_data.keys(), 'Population': api_data.values()}
    )
    dataframe = dataframe.sort_values(by='Population', ascending=False, ignore_index=True)[:10]
    dataframe.index += 1
    # dataframe = dataframe.style.format(
    #     precision=2, thousands=",", formatter={('Population'): '{:,.2f}'}
    # )

    return dataframe

# print(data_2021)

# dataframe = pd.DataFrame(
#         {'Country': data_2021.keys(), 'Population': data_2021.values()}
#     )
# dataframe = dataframe.sort_values(by='Population', ascending=False, ignore_index=True)[:10]
# dataframe.index += 1
# dataframe = dataframe.style.format(
#     precision=2, thousands=",", formatter={('Population'): '{:,.2f}'}
# )

api_data_2021 = fetch_api_data('tests/data2021.json')
api_data_2011 = fetch_api_data('tests/data2011.json')
api_data_2001 = fetch_api_data('tests/data2001.json')
dataframe = create_dataframe(api_data_2021)

dataList2021 = dataframe['Country'].tolist()
dataList2011 = [api_data_2011[keys] for keys in dataList2021]
dataList2001 = [api_data_2001[keys] for keys in dataList2021]

print(dataList2001)
# print(json_file[1][1]['country']['id'])
# print(json_file[1][1]['country']['value'])
# print(json_file[1][1]['value'])
# print(json_file[1][1]['date'])

# for i in json_file[1][1]['country']:
#     print(i[0])
# print(i['value'])