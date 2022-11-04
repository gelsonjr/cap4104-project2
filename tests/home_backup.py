import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

import altair as alt
import matplotlib.pyplot as plt

# To fetch data from World Bank API
# API_URL = 'https://api.worldbank.org/v2/en/country/all/indicator/SP.POP.TOTL?format=json&date=2019:2021&per_page=798'
API_URL = 'apps/data2019_2021.json' # temp

def fetch_api_data(api_url):
        dataset = []

        # response = requests.get(api_url)
        # json_file = response.json()

        with open(api_url, "r") as jf:
            json_file = json.load(jf)
        
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

    #st.markdown("### Line Chart")
    #st.line_chart(df)

    #bar_chart_data = df[df.columns[[1, 2]]]

    ######################################
    st.markdown("### Bar Chart: Country Population")
    y = {
        '2021': [1412000000, 1393000000, 331800000, 276000000, 225000000, 213999000, 211000000, 166000000, 143000000, 130000000]
        # '2020': [1411000000, 1380000000, 331000000, 273000000, 220000000, 212000000, 206000000, 164000000, 144000000, 128000000],
        # '2019': [1407000000, 1366000000, 328000000, 270000000, 216000000, 211000000, 200000000, 163000000, 144000000, 127000000]
    } 
    x = [
        'China', 'India', 'United States', 'Indonesia', 'Pakistan',
        'Brazil', 'Nigeria', 'Bangladesh', 'Russian Federation', 'Mexico'
    ]
    chart_data = pd.DataFrame(data=y, index=x)
    st.bar_chart(chart_data)
    ######################################

    z = {
        '2021': [1412000000, 1393000000, 331800000, 276000000, 225000000, 213999000, 211000000, 166000000, 143000000, 130000000],
        '2020': [1411000000, 1380000000, 331000000, 273000000, 220000000, 212000000, 206000000, 164000000, 144000000, 128000000],
        '2019': [1407000000, 1366000000, 328000000, 270000000, 216000000, 211000000, 200000000, 163000000, 144000000, 127000000]
    } 
    line_chart_data = pd.DataFrame(data=z, index=x)
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

