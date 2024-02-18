import streamlit as st
from constant import *
from component_files.info_section import create_info_section
from component_files.timeline_section import create_timeline_section
from component_files.chatbot_section import create_chatbot_section
from component_files.skill_section import create_skill_section
from component_files.medium_section import create_medium_section
from component_files.cert_section import create_cert_section
from component_files.contact_section import create_contact_section    
from component_files.hobbies_section import create_hobbies_section    


# for compatibility with chromaDB versioning
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


st.set_page_config(page_title='Jesse Henson' , layout="wide",page_icon='🏠')

st.image(info['Photo'])

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")

create_info_section()
create_chatbot_section()
create_timeline_section()

with st.container():

    col1,col2 = st.columns([0.5,0.5])
    with col1: 
        create_medium_section()
    with col2:
        create_skill_section()
with st.container():
    col1,col2 = st.columns([0.5,0.5])
    with col1:
        create_cert_section()
    with col2:
        create_contact_section()
with st.container():
    create_hobbies_section()


from streamlit.logger import get_logger

LOGGER = get_logger(__name__)




