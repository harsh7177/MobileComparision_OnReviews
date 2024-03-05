import streamlit as st
from scrapping import scrap,review_scrap,review_analysis

def show_explore_page(href):
    rev_df=review_scrap(href)
    st.dataframe(rev_df)
    

        
        
        
        
        