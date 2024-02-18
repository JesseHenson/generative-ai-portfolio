import streamlit as st
from streamlit_timeline import timeline

def create_timeline_section():
    with st.container():
        st.markdown("""""")
        st.subheader('📌 Career Snapshot')

        # load data
        with open('example.json', "r") as f:
            data = f.read()

        # render timeline
        timeline(data, height=400)