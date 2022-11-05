#import streamlit as st
from navigation import Navigation
from apps import home, map, feedback

# Gelson Cardoso Jr | PID: 6277187
# George Guardia | PID: 6119740
# Naor Vidal | PID: 6263881

# ------------------- APP SELECTION SECTION ---------------------
# This section provides different links to navigate between pages

app = Navigation()

app.add_app("Home", home.app)
app.add_app("Map", map.app)
app.add_app("Feedback", feedback.app)

app.run()
