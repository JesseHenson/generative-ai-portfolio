import streamlit as st
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.set_page_config(page_title='Hobbies' ,layout="wide",page_icon='🫶')
        
local_css("style/style.css")


st.sidebar.image(info['Photo'])


st.title("🫶 Hobbies")

col1, col2, col3 = st.columns(3)

with col1:
  st.write('Linux Distros')
   
with col2:
   st.write('Cooking')

with col3:
   st.write('Meditation')
   

