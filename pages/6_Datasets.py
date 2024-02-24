import json
from datetime import datetime
import streamlit as st
import requests
import utils

utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("📔 Datasets 📔")

with st.expander("**Kaggle Datasets**", expanded=True):
    st.markdown("""
    These are the datasets that I created by crawling various sites. The aggregated contents are pre-processed and 
    published on kaggle.
    
    **Tech**: Python, Requests, Beautiful Soup
    """)

tab_names = [
    "**Complete Works of Rabindranath Tagore**",
    "**Complete Works of Kazi Nazrul Islam**",
    "**Complete Works of Bankim Chandra**",
    "**Complete Works of Sarat Chandra**",
]
tab1, tab2, tab3, tab4 = st.tabs(tab_names)

with tab1:
    st.markdown("""
        **Dataset**: https://www.kaggle.com/datasets/aagalib/complete-works-of-rabindranath-tagore
        
        *This dataset contains a collection of 3438 literary items from all genres by Rabindranath Tagore.*
        """)

with tab2:
    st.markdown("""
        **Dataset**: https://www.kaggle.com/datasets/aagalib/complete-works-of-kazi-nazrul-islam
        
        *This dataset contains a collection of literary items from all genres by Kazi Nazrul Islam.*
        """)

with tab3:
    st.markdown("""
        **Dataset**: https://www.kaggle.com/datasets/aagalib/complete-works-of-bankim-chandra-chatterjee
        
        *This dataset contains a collection of literary items from all available genres by Bankim Chandra Chattopadhyay.*
        """)

with tab4:
    st.markdown("""
        **Dataset**: https://www.kaggle.com/datasets/aagalib/complete-works-of-sarat-chandra-chattopadhyay
        
        *This dataset contains a collection of literary items from all available genres by Sarat Chandra Chattopadhyay.*
        """)
