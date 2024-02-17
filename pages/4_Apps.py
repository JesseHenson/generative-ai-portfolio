import streamlit as st
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
st.set_page_config(page_title='Apps' ,layout="wide",page_icon='📱')

local_css("style/style.css")



app_arr = [
    {
    'subheader':'Upworkd Job Analysis',
    'gif':'./app_images/upworkd_ai.gif',
    'caption':'Get instant insight from a resume and a job description',
    'app_link':'https://upworkdjobanalysis-lb8srvd85rie6xbtne2pmz.streamlit.app/',
    'github_link':'https://github.com/JesseHenson/upworkd_job_analysis'
    },
{
    'subheader':'GIF Creator',
    'gif':'./app_images/gif_creator.gif',
    'caption':'Upload a video | get back a gif',
    'app_link':'https://make-a-gif-mlplve6smpn.streamlit.app',
    'github_link':'https://github.com/JesseHenson/Make-a-GIF'
    },
    {
    'subheader':'Web QA',
    'gif':'./app_images/web_qa.gif',
    'caption':'Give a URL and a question and get answer FAST',
    'app_link':'https://rag-generative-ai-5ireqvfsjr9.streamlit.app/',
    'github_link':'https://github.com/JesseHenson/rag-generative-ai'
    },
    {
    'subheader':'Upworkd Job Analysis',
    'gif':'./app_images/upworkd_ai.gif',
    'caption':'Get instant insight from a resume and a job description',
    'app_link':'https://upworkdjobanalysis-lb8srvd85rie6xbtne2pmz.streamlit.app/',
    'github_link':'https://github.com/JesseHenson/upworkd_job_analysis'
    },
]

with st.container():
    st.title("📱 Apps")
    col1, col2 = st.columns([1, 1])
    for i, app in enumerate(app_arr):
        if i % 2 == 0:
            with col1:
                st.subheader(app['subheader'])
                ncol1, ncol2, ncol3 = st.columns([.2,.6,.2])
                with ncol1:
                    st.page_link(app['app_link'], label="App")
                with ncol2:
                    st.image(app['gif'], 
                            caption=app['caption']
                            )
                with ncol3:
                    st.page_link(app['github_link'], label="Repo")
        else: 
            with col2:
                st.subheader(app['subheader'])
                ncol1, ncol2, ncol3 = st.columns([.2,.6,.2])
                with ncol1:
                    st.page_link(app['app_link'], label="App")
                with ncol2:
                    st.image(app['gif'], 
                            caption=app['caption']
                            )
                with ncol3:
                    st.page_link(app['github_link'], label="Repo")
    # with col1:
    #     st.subheader("Upworkd Job Analysis")
    #     st.image("./app_images/upworkd_ai.gif", 
    #             caption="Get instant insight from a resume and a job description"
    #             )
    #     st.page_link('https://upworkdjobanalysis-lb8srvd85rie6xbtne2pmz.streamlit.app/', label="App")
    #     st.page_link('https://github.com/JesseHenson/upworkd_job_analysis', label="Repo")
    # with col2: 
    #     st.subheader("Web QA")
    #     st.image("./app_images/web_qa.gif", 
    #             caption="Give a URL and a question and get answer FAST"
    #             )
    #     st.page_link('https://rag-generative-ai-5ireqvfsjr9.streamlit.app/', label="App")
    #     st.page_link('https://github.com/JesseHenson/rag-generative-ai', label="Repo")
    # with col1: 
    #     st.subheader("SQL: Under Constructions")
    # with col2: 
    #     st.subheader("GIF Creator")
    #     ncol1, ncol2, ncol3 = st.columns([.2,.6,.2])
    #     with ncol1:
    #         st.page_link('https://make-a-gif-mlplve6smpn.streamlit.app/', label="App")
    #     with ncol2:
    #         st.image("./app_images/gif_creator.gif", 
    #                 caption="Upload a video | get back a gif"
    #                 )
    #     with ncol3:
    #         st.page_link('https://github.com/JesseHenson/Make-a-GIF', label="Repo")
    # with col1:
    #     st.subheader("Tools Usage: Under Construction")
    # with col2: 
    #     st.subheader("API's In GenAI: Under Constructions")
    # with col1: 
    #     st.subheader("Graph DB Rag: Under Constructions")
    # with col2: 
    #     st.subheader("Autonomous Agents: Under Constructions")
    # with col2: 
    #     st.subheader("Chatbots: Under Constructions")