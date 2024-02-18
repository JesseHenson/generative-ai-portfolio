import streamlit as st
from constant import info

def create_contact_section():
    st.subheader("📨 Contact Me")
    contact_form = f"""
    <form action="https://formsubmit.co/{info["Email"]}" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)