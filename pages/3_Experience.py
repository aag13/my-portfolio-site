import json
from datetime import datetime
import streamlit as st
import requests
import utils

utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("📣 Experience 📣")

default_page_expand = False

with st.expander("**Software Engineer** at *BRAC IT*", expanded=default_page_expand):
    st.markdown("""
    *(January 2023 - Current)*
    
    **What I did**:
    - **Micro-Finance Field Applications**: Worked on the back-end application supporting multiple micro-finance field
    applications across different African countries. The core application is written in Django.
    - **Back-end Optimization**: Worked on code refactoring and optimization tasks to increase efficiency and response time.
    - **Knowledge Base**: Used ElasticSearch to design an internal knowledge base to aggregate and provide reference to root
    cause analysis reports.
    """)

with st.expander("**Lead Solutions Engineer** at *Shadhin Lab LLC*", expanded=default_page_expand):
    st.markdown("""
    *(February 2021 - December 2022)*
    
    **What I did**:
    
    - **Cloud Educational Platform**: Developed a full-fledged educational & training platform [CodersTrust](https://coderstrust.net/) serving 10k+
    learners using a suite of AWS services and Python as the runtime language.
    - **ML and Data Team**: Managed a team of Data Engineers to carry out various data pipeline and analytical tasks for
    in-house and client applications. Created a dataset of 6k+ processed bids from USA. Designed a bid classification model
    to automate the entire post-processing of bids.
    - **Crawling & Extraction Engine**: Created an asynchronous crawler engine that can handle multitude of bidding sites
    with unlimited variations as well as integration with various AWS services such as DynamoDB, Amazon OpenSearch,
    Amazon S3 etc. using Python & Beautiful Soup. Increased runtime efficiency by 94%.
    - **Bid Advisor Backend**: Developed the backend of [Bid Advisor](https://bidadvisor.xyz) platform to support the API needs from client and
    admin applications as well as integration with the crawling module.
    """)

with st.expander("**Full Stack Developer** at *BDEMR Solutions Corp.*", expanded=default_page_expand):
    st.markdown("""
    *(February 2019 - December 2020)*
    
    **What I did**:
    
    - **Healthcare Applications**: Worked on frontend and backend of multiple healthcare applications for clinics, doctors and
    end-user patients using Polymer, Angular (frontend) and ExpressJS (backend).
    - **Maintenance & Refactoring**: Maintained and refactored existing code bases of highly integrated enterprise
    applications.
    - **Collaborating with Healthcare Professionals**: Interacted with healthcare professionals to introduce new modules as
    well as improving the user experience of existing features.
    - **Analytical Tasks on Antibiotic Resistance**: Developed a reporting mechanism with complex filtering to facilitate
    medication decisions based on cumulative efficacy reports which is currently used in BSMMU ICU division.
    """)

with st.expander("**Course Contractual Faculty** at *BRAC University*", expanded=default_page_expand):
    st.markdown("""
    *(January 2020 - January 2021)*
    
    **What I did**:
    
    - **Conducting Class**: Conducted theory-lab classes and tutorial sessions for a 3-credit course (CSE471 - Systems Analysis
    and Design).
    - **Preparing Course Materials**: Prepared lecture notes, quizzes, assignments, lab class materials, mid-term and final
    question papers.
    - **Grading Scripts**: Graded quizzes, assignments, mid-term and final scripts, lab assignments and provided feedback on
    lab tasks.
    """)

with st.expander("**Co-Founder & Lead Developer** at *Auvenora*", expanded=default_page_expand):
    st.markdown("""
    *(June 2018 - December 2019)*
    
    **What I did**:
    
    - **Requirement Analysis and System Design**: Gathered software requirements through interviews with clients and
    domain experts and designed and developed an entire pharmacy management system.
    - **Maintenance & Refactoring**: Provided software maintenance and client support.
    """)

with st.expander("**Technical Operations Consultant** at *Dassault Systemes Innovation Technologies*", expanded=default_page_expand):
    st.markdown("""
    *(February 2018 - April 2018)*
    
    **What I did**:
    
    - **Root Cause Analysis & Debugging**: Coordinated efforts to solve software issues and resume full operational
    capability for mission critical systems by sifting through thousands of log files and relevant system architectures.
    - **Collaboration**: Collaborated with software forensics and specialists located in different geographical regions to provide
    accurate and timely support for red alert issues.
    """)

with st.expander("**Teaching Assistant** at *BRAC University*", expanded=default_page_expand):
    st.markdown("""
    *(January 2016 - December 2016)*
    
    **What I did**:
    
    - **Conducting Tutorial Session**: Assisted students in understanding course materials and helped them in their course assignments.
    """)

