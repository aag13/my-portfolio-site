import json
from datetime import datetime
from pathlib import Path
import streamlit as st
import requests
import utils

utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("💎 Projects 💎")

default_page_expand = False

with st.expander("**Crawling of Bidding and RFP Sites**", expanded=default_page_expand):
    st.markdown(f"""
    Architected a generic crawler where hundreds of bidding sites from dozens of states in the USA are crawled daily to 
    extract structured and formatted bids/RFPs, from each site.
    - The key part of the crawler is its ability to handle hundreds of sites with completely different structures and content layouts.
    - Created an orchestrator to initiate daily crawling and manage all the sites by ensuring proper logging and error handling.
    - Log archives and supplementary documents for each bid were stored in Amazon S3.
    - Amazon Eventbridge rules were used to trigger crawling jobs daily at a specific time.
    - Amazon Opensearch was used as the primary storage of formatted bidding items and to provide full-text search functionalities.
    - Thousands of bids from hundreds of sites were put into Amazon SQS message queues for efficient processing of documents.
    - The project was hosted on and run with AWS Fargate.
    
    **Tech**: Python, Requests, BeautifulSoup, Amazon S3, Eventbridge, Opensearch, SQS, AWS Fargate.

    **Project**: https://www.bidadvisor.xyz/client/home
    """)

with st.expander("**Asynchronous Crawler-Scraper Architecture**",
                 expanded=default_page_expand):
    st.markdown(f"""
    This was the asynchronous version of the *Bid Crawler* that reduced the crawling time by more than 85% by introducing 
    asynchronous processing at three nested levels, namely the site-level, page-level, and individual bid-level.
    - Asynchronous orchestrator initiated the crawling for each site using event loop.
    - Amazon DynamoDB was used for storing management and tracking logs for each bid. These documents were used to 
    re-crawl or skip sites or pages based on some predefined heuristics.
    - AsyncIO and AIOHTTP were used for asynchronous API calls.
    
    **Tech**: Python, Requests, BeautifulSoup, Amazon DynamoDB, AsyncIO, AIOHTTP.
    """)

    st.image("assets/crawler-architecture.jpg", caption="Crawler Architecture", use_column_width=True)


with st.expander("**Crawling, Scraping, Data Mining**", expanded=default_page_expand):
    st.markdown("""
    Expertise in the field of crawling and scraping data from a large number of sites on the internet. Experienced with 
    various rate-limiting and paywall prevention techniques.
    - Crawled and scraped market information from Dhaka Stock Exchange for hundreds of companies to create a dataset to 
    be used in time-series analysis of stock prices.
    - Crawled official sites to compose collection of literary works from multiple classical Bengali writers to be used 
    in literary analysis and NLP projects. Created complex parsing and extraction rules in order to generate entire 
    collection of a writer’s literary works.
    - Created a scraping module to collect article metadata from *The New York Times* API for a research group on media bias
    analysis.
    
    **Tech**: Python, Requests, BeautifulSoup, Scrapy, BeautifulSoup, Selenium.

    **Project**: 
    - https://www.kaggle.com/aagalib/datasets
    - https://www.dsebd.org/company_listing.php
    - 
    """)

with st.expander("**PayPal Integration with AWS**", expanded=default_page_expand):
    st.markdown("""
    Integrated the Paypal payment system with backend cloud applications running on AWS using webhooks to 
    support online content purchases for thousands of customers in a large-scale application. 

    **Tech**: Python, AWS, PayPal API.

    **Project**: https://www.coderstrust.net/
    """)

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
