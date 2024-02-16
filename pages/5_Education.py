import streamlit as st
from streamlit_timeline import timeline
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
st.set_page_config(page_title='Education' ,layout="wide",page_icon='🎓')

local_css("style/style.css")

st.sidebar.image(info['Photo'])

st.title("🎓 Education")

# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('education.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)