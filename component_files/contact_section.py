import streamlit as st
import base64
from constant import info

def create_contact_section():
    st.subheader("📨 Contact Me")

    col1, col2, col3, col4 = st.columns([2,1,1,1])
    with col1:
        st.markdown("""<a href="mailto:henson.jhenson.jesse@gmail.com" style='text-decoration:none'>Contact us!</a>"""
                    , unsafe_allow_html=True)
    with col2:
        st.markdown(
            """<a href="https://github.com/JesseHenson">
            <img src="data:images/github.png;base64,{}" width="25">
            </a>""".format(
                base64.b64encode(open("images/github.png", "rb").read()).decode()
            ),
        unsafe_allow_html=True,
    )
    with col3:
        st.markdown(
            """<a href="https://medium.com/@jesse.henson">
            <img src="data:images/medium.png;base64,{}" width="25">
            </a>""".format(
                base64.b64encode(open("images/medium.png", "rb").read()).decode()
            ),
        unsafe_allow_html=True,
    )
    with col4: 
        st.markdown(
        """<a href="https://www.linkedin.com/in/jessehensonai">
        <img src="data:images/linkedin.png;base64,{}" width="25">
        </a>""".format(
            base64.b64encode(open("images/linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
