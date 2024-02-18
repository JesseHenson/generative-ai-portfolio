import streamlit as st
from constant import info

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: radial-gradient(circle at right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

def create_info_section():
    with st.container():
        col1,col2 = st.columns([8,3])

    full_name = info['Full_Name']
    with col1:
        gradient('#2D3250','#424769','#FFFFFF',f"Hi, I'm {full_name}👋", info["Intro"])
        st.write("")
        st.write(info['About'])
    