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

    # for index in range(len(json_file[1])):
    #     data.append({
    #         json_file[1][index]['country']['value']: json_file[1][index]['value']
    #         # "Country": json_file[1][index]['country']['value'],
    #         # "Population": json_file[1][index]['value'],
    #     })
    
    # data = data[49:] # The first 49 elements from the data set are not countries

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
    #df = create_table()

    # url2021 = 'apps/jason2021.json'
    # url2020 = 'apps/jason2020.json'
    
    # api_data_2021 = fetch_api_data('apps/data2021.json')
    # dataframe_2021 = create_dataframe(api_data_2021)

    # api_data_2011 = fetch_api_data('apps/data2011.json')
    # dataframe_2011 = create_dataframe(api_data_2011)

    # api_data_2001 = fetch_api_data('apps/data2001.json')
    # dataframe_2001 = create_dataframe(api_data_2001)

    st.dataframe(df.style.format(subset=['Population'], formatter='{:,.2f}'))

    #st.dataframe(dataframe_2011)
    #st.dataframe(dataframe_2001)
    #st.dataframe(df2020)

    #st.write('Navigate to `Data Stats` page to visualize the data')

    #st.markdown("### Line Chart")
    #st.line_chart(df)

    #bar_chart_data = df[df.columns[[1, 2]]]

    ######################################
    st.markdown("### Bar Chart: Country Population")

    x_axis = countries_list
    y_axis = {
        # 'Population in  2001': population_2001,
        # 'Population in  2011': population_2011,
        'Population in 2021': population_2021
    }

    # y = {
    #     '2021': [1412000000, 1393000000, 331800000, 276000000, 225000000, 213999000, 211000000, 166000000, 143000000, 130000000]
    #     # '2020': [1411000000, 1380000000, 331000000, 273000000, 220000000, 212000000, 206000000, 164000000, 144000000, 128000000],
    #     # '2019': [1407000000, 1366000000, 328000000, 270000000, 216000000, 211000000, 200000000, 163000000, 144000000, 127000000]
    # } 
    # x = [
    #     'China', 'India', 'United States', 'Indonesia', 'Pakistan',
    #     'Brazil', 'Nigeria', 'Bangladesh', 'Russian Federation', 'Mexico'
    # ]
    # chart_data = pd.DataFrame(data=y_axis, index=x_axis)
    bar_chart_data = pd.DataFrame(
        data={'Population in 2021': population_2021},
        index=countries_list
    )
    st.bar_chart(bar_chart_data)

    ######################################
    st.markdown("### Line Chart: Country Population Growth Since 2001")

    z = {
        '2021': [1412000000, 1393000000, 331800000, 276000000, 225000000, 213999000, 211000000, 166000000, 143000000, 130000000],
        '2020': [1411000000, 1380000000, 331000000, 273000000, 220000000, 212000000, 206000000, 164000000, 144000000, 128000000],
        '2019': [1407000000, 1366000000, 328000000, 270000000, 216000000, 211000000, 200000000, 163000000, 144000000, 127000000]
    } 
    # line_chart_data = pd.DataFrame(data=z, index=x)
    line_chart_data = pd.DataFrame(
        data={
            '2001': population_2001,
            '2011': population_2011,
            '2021': population_2021
        },
        index=countries_list)
    st.line_chart(line_chart_data)





    # Matplotlib test
    # st.markdown("### Pyplot")
    # x = np.arange(5)
    # y1 = [34, 56, 12, 89, 67]
    # y2 = [12, 56, 78, 45, 90]
    # y3 = [14, 23, 45, 25, 89]
    # width = 0.2
    # # plot data in grouped manner of bar type
    # plt.bar(x-0.2, y1, width, color='cyan')
    # plt.bar(x, y2, width, color='orange')
    # plt.bar(x+0.2, y3, width, color='green')
    # plt.xticks(x, ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'])
    # plt.xlabel("Teams")
    # plt.ylabel("Scores")
    # plt.legend(["Round 1", "Round 2", "Round 3"])
    # st.pyplot(plt)
    #plt.show()

