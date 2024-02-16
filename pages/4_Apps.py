import streamlit as st
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.set_page_config(page_title='Apps' ,layout="wide",page_icon='📱')

st.sidebar.image(info['Photo'])


with st.container():
    st.title("📱 Apps")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Upworkd Job Analysis")
        st.image("./app_images/upworkd_ai.gif", 
                caption="Get instant insight from a resume and a job description"
                )
        st.page_link('https://upworkdjobanalysis-lb8srvd85rie6xbtne2pmz.streamlit.app/', label="App")
        st.page_link('https://github.com/JesseHenson/upworkd_job_analysis', label="Repo")
    with col2: 
        st.subheader("QA: Under Constructions")
    with col1: 
        st.subheader("SQL: Under Constructions")
    with col2: 
        st.subheader("Chatbots: Under Constructions")
    with col1:
        st.subheader("Tools Usage: Under Construction")
    with col2: 
        st.subheader("API's In GenAI: Under Constructions")
    with col1: 
        st.subheader("Graph DB Rag: Under Constructions")
    with col2: 
        st.subheader("Autonomous Agents: Under Constructions")