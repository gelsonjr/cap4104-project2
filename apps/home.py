import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

# To fetch data from World Bank API
# API_URL = 'https://api.worldbank.org/v2/en/country/all/indicator/SP.POP.TOTL?format=json&date=2019:2021&per_page=798'
API_URL = 'apps/data2019_2021.json' # temp

def fetch_api_data(api_url):
        dataset = []

        response = requests.get(api_url)
        json_file = response.json()

        # with open(url, "r") as jf:
        #     json_file = json.load(jf)
        
        for index in range(0, len(json_file[1]) - 2, 3):
            dataset.append({
                'Code': json_file[1][index]['country']['id'],
                'Country': json_file[1][index]['country']['value'],
                'Population in 2019': json_file[1][index + 2]['value'],
                'Population in 2020': json_file[1][index + 1]['value'],
                'Population in 2021': json_file[1][index]['value'],
            })

        df = pd.DataFrame(data=dataset[49:])
        df = df[df.columns[[1, 2, 3, 4]]]
        df = df.sort_values(by='Population in 2021', ascending=False, ignore_index=True)[:10]
        df.index += 1
        df = df.style.format(precision=2, thousands=",", formatter={(
            'Population in 2019',
            'Population in 2020',
            'Population in 2021'): '{:,.2f}'
        })
        
        return df

# def fetch_api_data_LINE(url):
#         dataset = []

#         with open(url, "r") as jf:
#             json_file = json.load(jf)
        
#         for index in range(len(json_file[1])):
#             dataset.append({
#             "Code": json_file[1][index]['country']['id'],
#             "Country": json_file[1][index]['country']['value'],
#             "Population": json_file[1][index]['value'],
#             "Year": json_file[1][index]['date']
#         })

#         df = pd.DataFrame(data=dataset[49:])
#         df = df[df.columns[[1, 2, 3]]]
#         df = df.sort_values(by='Population', ascending=False, ignore_index=True)[:10]
#         df.index += 1
#         df = df.style.format({'Population': '{:,.2f}'})
        
#         return df

def app():
    st.title('Home')

    #st.write("This is a sample home page in the mutliapp.")
    #st.write("See `apps/home.py` to know how to use it.")

    st.markdown("### Top 10 Most Populous Countries in the World")
    #df = create_table()

    # url2021 = 'apps/jason2021.json'
    # url2020 = 'apps/jason2020.json'
    
    
    df = fetch_api_data(API_URL)
    #df2020 = fetch_api_data(url2020)



    st.dataframe(df)
    #st.dataframe(df2020)

    #st.write('Navigate to `Data Stats` page to visualize the data')

    st.markdown("### Line Chart")
    st.line_chart(df)


