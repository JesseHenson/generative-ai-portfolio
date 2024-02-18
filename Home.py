import streamlit as st
from constant import *
from component_files.info_section import create_info_section
from component_files.timeline_section import create_timeline_section
from component_files.chatbot_section import create_chatbot_section
from component_files.skill_section import create_skill_section
from component_files.medium_section import create_medium_section
from component_files.cert_section import create_cert_section
from component_files.contact_section import create_contact_section    


# for compatibility with chromaDB versioning
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')



st.set_page_config(page_title='Jesse Henson' ,layout="wide",page_icon='🏠')

st.image(info['Photo'])

create_info_section()

create_chatbot_section()

create_skill_section()
    
create_timeline_section()


with st.container():
    st.markdown("""""")
    st.subheader('✍️ Medium')
    col1,col2 = st.columns([0.95, 0.05])
    with col1: 
        create_medium_section()
    with st.container():
        col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
        with col1:
            create_cert_section()
        with col2:
            create_contact_section()


from streamlit.logger import get_logger

LOGGER = get_logger(__name__)




