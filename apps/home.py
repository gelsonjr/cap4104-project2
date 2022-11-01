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
    #df = pd.read_json("apps/clean_jason.json") #works

    with open("apps/clean_jason.json", "r") as jf:
        json_file = json.load(jf)

    json_data = pd.json_normalize(json_file) # organizes data 
    json_data.drop(json_data.columns[[0, 3, 4, 5, 6, 7, 8]], axis=1, inplace=True) # removes unwanted columns
    df = json_data[json_data.columns[[2, 1, 0]]] # reorder columns
    df = df.rename(
        columns={
            'country.value' : 'Country',
            'value' : 'Population',
            'date' : 'Year'
        }
    )

    df = df.sort_values(by='value', ascending=False)

    st.write(df)

    st.write('Navigate to `Data Stats` page to visualize the data')


