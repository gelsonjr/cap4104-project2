import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

import json

def app():
    st.title('Home')

    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")

    st.markdown("### Sample Data")
    #df = create_table()

    # with open("apps/clean_jason.json", "r") as jf:
    #     json_file = json.load(jf)

    with open("apps/jason300.json", "r") as jf:
        json_file = json.load(jf)
    
    # st.dataframe(json_file[1])

    # adds data to dataframe, organizes, removes unwanted columns, reorder, etc
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

    st.dataframe(df.style.format({'Population': '{:,.2f}'}))

    st.write('Navigate to `Data Stats` page to visualize the data')


