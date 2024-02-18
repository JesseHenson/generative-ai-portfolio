import streamlit as st
import streamlit.components.v1 as components

from constant import info, embed_rss

def create_medium_section():
    st.subheader('✍️ Medium')
    with st.expander('Display my latest posts'):
        components.html(embed_rss['rss'],height=400)
        
    st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Medium']), unsafe_allow_html=True)