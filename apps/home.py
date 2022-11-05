import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

# CAP 4104 | Fall 2022 | Project #2 - UI/UX Design with Streamlit
# Gelson Cardoso Jr | PID: 6277187
# George Guardia | PID: 6119740
# Naor Vidal | PID: 


# ----------------------- MAIN SECTION --------------------------
# This section displays the 10 most populous countries in the world,
# along with their population and growth since 2001 

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
    data = {}

    # response = requests.get(api_url)
    # json_file = response.json()

    with open(api_url, "r") as jf:
        json_file = json.load(jf)
    
    # Parsing JSON payload into a clean, {Country: Population} dictionary
    for index in range(50, len(json_file[1])):
        data.update({
            json_file[1][index]['country']['value']: json_file[1][index]['value']
        })

    return data

# This method creates a pandas dataframe based on data fetched from World Bank API
def create_dataframe(api_data):
    dataframe = pd.DataFrame(
        {'Country': api_data.keys(), 'Population': api_data.values()}
    )
    dataframe = dataframe.sort_values(by='Population', ascending=False, ignore_index=True)[:10]
    dataframe.index += 1

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

    display_students = st.checkbox('Student Information')
    if display_students:
        st.text_area(
            'CAP 4104 | Fall 2022 | Project #2 - UI/UX Design with Streamlit',
            '''Gelson Cardoso Jr | PID: 6277187\nGeorge Guardia | PID: 6119740\nNaor Vidal | PID: '''
        )      

    # ----------------------- INTERACTIVE TABLE --------------------------
    st.markdown("### Top 10 Most Populous Countries in the World")
    st.dataframe(df.style.format(subset=['Population'], formatter='{:,.2f}'), use_container_width=True)
    st.info("Data Source: World Bank - Population, total. www.worldbank.org (2021)")

    # ----------------------- BAR CHART --------------------------
    st.markdown("### Country Population Comparasion")
    bar_chart_data = pd.DataFrame(
        data={
            'Population in 2021': population_2021
        },
        index=countries_list
    )
    st.bar_chart(bar_chart_data)
    st.info("Data Source: World Bank - Population, total. www.worldbank.org (2021)")

    # ----------------------- LINE CHART --------------------------
    st.markdown("### Country Population Growth In The Last 20 Years")
    line_chart_data = pd.DataFrame(
        data={
            '2001': population_2001,
            '2011': population_2011,
            '2021': population_2021
        },
        index=countries_list
    )
    st.line_chart(line_chart_data)
    st.info("Data Source: World Bank - Population, total. www.worldbank.org (2001, 2011, and 2021)")
