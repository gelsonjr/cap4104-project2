import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

import altair as alt
import matplotlib.pyplot as plt

API_URL_2021_DATA = 'apps/data2021.json'
API_URL_2011_DATA = 'apps/data2011.json'
API_URL_2001_DATA = 'apps/data2001.json'

# API_URL = 'https://api.worldbank.org/v2/en/country/all/indicator/SP.POP.TOTL?format=json&per_page=300&date='
# API_URL_2021_DATA = API_URL + '2021'
# API_URL_2011_DATA = API_URL + '2011'
# API_URL_2001_DATA = API_URL + '2001'

# This method fetches data from World Bank API, and parses the JSON payload
# to store only the relevant information (countries & populations)
def fetch_api_data(api_url):
    # data = []
    data = {}

    # response = requests.get(api_url)
    # json_file = response.json()

    with open(api_url, "r") as jf:
        json_file = json.load(jf)
    
    for index in range(50, len(json_file[1])):
        data.update(
            {json_file[1][index]['country']['value']: json_file[1][index]['value']}
        )

    return data

# This method creates a pandas dataframe based on data fetched from World Bank API
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

def app():
    data_2001 = fetch_api_data(API_URL_2001_DATA)
    data_2011 = fetch_api_data(API_URL_2011_DATA)
    data_2021 = fetch_api_data(API_URL_2021_DATA)

    df = create_dataframe(data_2021)

    countries_list = df['Country'].tolist()
    population_2001 = [data_2001[key] for key in countries_list]
    population_2011 = [data_2011[key] for key in countries_list]
    population_2021 = [data_2021[key] for key in countries_list]

    st.title('Home')

    #st.write("This is a sample home page in the mutliapp.")
    #st.write("See `apps/home.py` to know how to use it.")

    st.markdown("### Top 10 Most Populous Countries in the World")

    st.dataframe(df.style.format(subset=['Population'], formatter='{:,.2f}'))

    ######################################
    st.markdown("### Bar Chart: Country Population")

    x_axis = countries_list
    y_axis = {
        # 'Population in  2001': population_2001,
        # 'Population in  2011': population_2011,
        'Population in 2021': population_2021
    }

    bar_chart_data = pd.DataFrame(
        data={'Population in 2021': population_2021},
        index=countries_list
    )
    st.bar_chart(bar_chart_data)

    ######################################
    st.markdown("### Line Chart: Country Population Growth Since 2001")

    line_chart_data = pd.DataFrame(
        data={
            '2001': population_2001,
            '2011': population_2011,
            '2021': population_2021
        },
        index=countries_list)
    st.line_chart(line_chart_data)
