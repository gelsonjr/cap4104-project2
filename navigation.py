import streamlit as st

# Gelson Cardoso Jr | PID: 6277187
# George Guardia | PID: 6119740
# Naor Vidal | PID: 6263881

# ----------------- NAVIGATION SECTION -------------------
# Helper section used for app switching within the sidebar

class Navigation:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.radio(
            'Go To',
            self.apps,
            format_func=lambda app: app['title']
        )

        app['function']()
