import streamlit as st

from constant import info

def create_hobbies_section():
    st.subheader("🤖 Hobbies")
    hobbies = info['Hobbies']
    st.info(' | '.join(hobbies))