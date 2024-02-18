import streamlit as st

def create_cert_section():
    
    st.subheader("👨‍🎓 ML Certifications")
    col1, col2 = st.columns([.5,.5])
    with col1:
        st.image("./images/azure.png", caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with col2:
        st.image("./images/AWS.png", caption=None, width=80, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
