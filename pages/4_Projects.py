import json
from datetime import datetime
import streamlit as st
import requests
import utils

utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("💎 Projects 💎")

default_page_expand = False

with st.expander("**confiGOAT (Python Package)**", expanded=default_page_expand):
    st.markdown("""
    **[confiGOAT](https://pypi.org/project/configoat/)** is a powerful, flexible, and developer-friendly management tool 
    for all your environment variables and configurations.
    
    **Tech**: Python
    
    **Source**: https://github.com/aag13/configoat
    """)

with st.expander("**Course Recommender Bot**", expanded=default_page_expand):
    st.markdown("""
    A chatbot that suggests courses based on users’ profiles using a MOOC course database.
    
    **Tech**: Python, Streamlit, OpenAI, Chroma Vector Database, LangChain
    
    **Source**: https://github.com/aag13/chatbot-course-recommender
    """)

with st.expander("**Career Guidance Bot**", expanded=default_page_expand):
    st.markdown("""
    A chatbot providing career guidance based on users’ profile parameters.

    **Tech**: Python, Streamlit, OpenAI

    **Source**: https://github.com/aag13/openai-chatbot
    """)

with st.expander("**AI Proofreader**", expanded=default_page_expand):
    st.markdown("""
    Designing a serverless application on AWS using OpenAI to proofread users’ contents.

    **Tech**: Python, AWS, OpenAI
    """)

with st.expander("**Solar Panel Detection from Satellite Images**", expanded=default_page_expand):
    st.markdown("""
    Fine-tuning a pre-trained CNN model to detect solar panels in satellite images.

    **Tech**: Python, PyTorch, Google Maps
    """)

with st.expander("**RabindraNet**", expanded=default_page_expand):
    st.markdown("""
    Creating Literary Works in the Style of Rabindranath Tagore: A character level RNN model with
    stacked-LSTM layers trained on the works of Rabindranath Tagore to produce literary works in his style for multiple genres.
    
    **Tech**: TensorFlow, Google Colab

    **Source**: https://arxiv.org/pdf/2202.00481.pdf
    """)

with st.expander("**shop-A-shop**", expanded=default_page_expand):
    st.markdown("""
    An online marketplace to buy, sell, manage, and communicate all in one designed to support small and medium
    entrepreneurs during Covid.

    **Tech**: Flutter, Firebase

    **Source**: https://play.google.com/store/apps/details?id=com.auvenora.shopashop&hl=en
    """)

with st.expander("**Data Structure Visualization Application**", expanded=default_page_expand):
    st.markdown("""
    Flow chart to code generator and data structure visualization application.

    **Tech**: JAVA, Swing Widget Toolkit

    **Source**: https://github.com/aag13/visualization-application
    """)

with st.expander("**agroSoft**", expanded=default_page_expand):
    st.markdown("""
    An agricultural management application with primary focus on crop prediction.

    **Tech**: PHP, HTML, CSS, JavaScript, MySQL

    **Source**: https://github.com/aag13/agriculture-project
    """)


# with st.expander("****", expanded=default_page_expand):
#     st.markdown("""
#
#
#     **Tech**:
#
#     **Source**:
#     """)
