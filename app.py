import streamlit as st
from multiapp import MultiApp
from apps import home, map, feedback

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Map", map.app)
app.add_app("Feedback", feedback.app)

# The main app
app.run()