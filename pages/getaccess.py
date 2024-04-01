import streamlit as st
from database import find_api_key
from pymongo import MongoClient

def main():    
    st.set_page_config(page_title="Get Access", page_icon=":penguin:")
    st.title(':penguin: Say Hi to your best friend')
    st.subheader('This service requires special access')

    st.markdown("Demo by [Qiang Li](https://www.linkedin.com/in/qianglil/). All rights reserved.")

    # hdie sidebar
    st.markdown("""
        <style>
            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }
        </style>
        """, unsafe_allow_html=True)
    
    # this markdown is for hiding "github" button
    st.markdown("<style>#MainMenu{visibility:hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<style>footer{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<style>header{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{display: none;} 
    </style>
    """,
    unsafe_allow_html=True
    )

    api_key = st.text_input("Please enter your access code to continue (DM me on Linkedin to get access)", type="password")
    if api_key:
        # check if api_key is valid
        if find_api_key(api_key):
            # continue with service
            st.text("Please follow the steps below to use the service:")
            st.text("1. Download telegram app on your device")
            st.text("2. Start telegram app and find your best friend bot by seraching 'friendbot'")
            st.text("3. Follow the instruction menu to use the service. Enjoy!")
            
        else:
            st.warning("access code is invalid, please retry or get new code")

    
if __name__ == '__main__':
    main()