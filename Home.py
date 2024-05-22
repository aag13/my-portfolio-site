import json
from datetime import datetime
import streamlit as st
import requests
import utils


utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("🎉 You have reached Asadullah Al Galib 🎉")

default_page_expand = True

with st.expander("Bio 📖", expanded=default_page_expand):
    st.markdown("""
    I am **Asadullah Al Galib**, a backend developer with over 5 years of experience, specializing in AWS and Data Engineering. 📓
    
    I started my career as a Full Stack developer working with NodeJS and PolymerJS (I know 👀). Over the years, I got my feet wet 
    with Python web frameworks, large-scale web crawling, and various machine learning and data science projects. I have worked on 
    many serverless and server-based backend applications. I have designed large-scale applications from scratch as well as 
    refactored complex systems to increase efficiency and make them more performant. 🚀
    
    Solving problems with simple, well-designed and effective solutions that have real-world impacts on people's lives 
    is what motivates me and keeps me going. 🧭
    
    ---
    
    **Ideal day at work:** 
    - Design a large-scale data engineering pipeline (Crawling, Scraping, ETL, Data Lake, Data Warehouse).
    - Research, query, and data analysis. Extract insights from the data.
    - Design and set up backend system to support various dashboard and downstream tasks.
    - Scale Scale Scale. Make it secure and performant.
    - *(Sometimes run ML models, train, test, evaluate, and deploy on production)*
    """)

col1, col2 = st.columns(2)

with col1:
    with st.expander("Social Links 🔗", expanded=default_page_expand):
        st.markdown("""
        **GitHub**: https://github.com/aag13?tab=repositories
        
        **LinkedIn**: https://linkedin.com/in/asadullah-al-galib-186685118/
        
        **Kaggle**: https://kaggle.com/aagalib/datasets
        
        **Medium**: https://medium.com/@asadullahgalib13
        """)

with col2:
    with st.expander("Contact ✉️", expanded=default_page_expand):
        st.markdown("""
        **Email**: *asadullahgalib13[at]gmail[dot]com*
        """)

