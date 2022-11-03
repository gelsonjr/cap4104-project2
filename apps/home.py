import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

import json

def fetch_api_data(url):
        # with open("apps/jason2021.json", "r") as jf:
        with open(url, "r") as jf:
            json_file = json.load(jf)
        json_data = pd.json_normalize(json_file[1][49:])
        json_data.drop(json_data.columns[[0, 3, 4, 5, 6, 7, 8]], axis=1, inplace=True)
        df = json_data[json_data.columns[[2, 1, 0]]]
        df = df.rename(
            columns={
                'country.value' : 'Country',
                'value' : 'Population',
                'date' : 'Year'
            }
        )
        df = df.sort_values(by='Population', ascending=False, ignore_index=True)[:10]
        df['Population'] = df['Population'].astype(float)
        df.index += 1
        df = df.style.format({'Population': '{:,.2f}'})
        return df


def app():
    st.title('Home')

    #st.write("This is a sample home page in the mutliapp.")
    #st.write("See `apps/home.py` to know how to use it.")

    st.markdown("### Top 10 Most Populous Countries in the World")
    #df = create_table()

    # with open("apps/clean_jason.json", "r") as jf:
    #     json_file = json.load(jf)



    # with open("apps/jason2021.json", "r") as jf:
    #     json_file = json.load(jf)
    
    # # adds data to dataframe, organizes, removes unwanted columns, reorder, etc
    # json_data = pd.json_normalize(json_file[1][49:])
    # json_data.drop(json_data.columns[[0, 3, 4, 5, 6, 7, 8]], axis=1, inplace=True)
    # df = json_data[json_data.columns[[2, 1, 0]]]
    # df = df.rename(
    #     columns={
    #         'country.value' : 'Country',
    #         'value' : 'Population',
    #         'date' : 'Year'
    #     }
    # )
    # df = df.sort_values(by='Population', ascending=False, ignore_index=True)[:10]
    # df['Population'] = df['Population'].astype(float)
    # df.index += 1
    # df = df.style.format({'Population': '{:,.2f}'})


    url2021 = 'apps/jason2021.json'
    url2020 = 'apps/jason2020.json'
    df2021 = fetch_api_data(url2021)
    df2020 = fetch_api_data(url2020)



    st.dataframe(df2021)
    st.dataframe(df2020)

    #st.write('Navigate to `Data Stats` page to visualize the data')

    st.markdown("### Line Chart")

    st.line_chart(df)


