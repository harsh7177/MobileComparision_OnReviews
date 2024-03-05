import streamlit as st
from Products import show_predict_page
from explore_page import show_explore_page
from review_page import show_keyword_page
import textwrap
from scrapping import scrap,review_scrap



page = st.sidebar.selectbox("Reviews Or Query Reviews", ("Product Info", "Review Analysis"))






if page=="Product Info":
    pro1 = st.text_input("First Device to compare")
    pro2 = st.text_input("Second Device to compare")
    if st.button('Search'):
        if len(pro1)>0 and len(pro2):
            show_predict_page(pro1,pro2)

elif page=="Review Analysis":
    pro1 = st.text_input("1st Device to compare", "1st")
    pro2 = st.text_input("2nd Device to compare", "2nd")
    keyword=st.text_input('Keyword To Query Reviews:-')
    if len(keyword)>0:
        show_keyword_page(pro1,pro2,keyword)
        
st.sidebar.divider()
st.sidebar.caption('**Empower your device purchasing decisions with insightful comparisons fueled by real user reviews posted on FLIPKART. My Streamlit-powered app lets you effortlessly compare two mobile models based on authentic Flipkart reviews, giving you the clarity you need to make informed choices. Experience the future of device comparison today!**')
st.sidebar.divider()
st.sidebar.caption("<p style='text-align:center'>Made by Harsh</p>",unsafe_allow_html=True)
        


