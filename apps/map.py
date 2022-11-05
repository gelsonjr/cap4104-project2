import streamlit as st
import pandas as pd

# ----------------------- MAP SECTION --------------------------
# This section displays the map location of the 10 most populous
# countries in the world

def app():
    coordinates = [
        [35.8617, 104.1954],  # China
        [20.5937, 78.9629],   # India
        [39.0000, -80.5000],  # United States
        [0.7893, 113.9213],   # Indonesia
        [30.3753, 69.3451],   # Pakistan
        [-14.2350, -51.9253], # Brazil
        [7.48906, 9.05804],   # Nigeria
        [23.6850, 90.3563],   # Bangladesh
        [61.5240, 105.3188],  # Russian Federation
        [23, -102]            # Mexico
    ]

    st.title('Map')

    st.markdown("### Location of the 10 most populous countries in the world")
    world_map = pd.DataFrame(
        coordinates, 
        columns = ['lat', 'lon']
    )
    st.map(world_map, zoom=1)
