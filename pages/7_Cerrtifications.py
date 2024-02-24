import json
from datetime import datetime
import streamlit as st
import requests
import utils

utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("📝 Certifications 📝")

default_page_expand = True

st.markdown("""
These are the certificates that I have acquired from various MOOC and learning platforms to further my understanding in 
Machine Learning and Data Science.
""")

with st.expander("**Coursera**", expanded=default_page_expand):
    st.markdown("""
    - [Deep Learning Specialization](https://www.coursera.org/account/accomplishments/specialization/certificate/ZC5GKBXELEXM)
    - [Convolutional Neural Networks](https://www.coursera.org/account/accomplishments/certificate/BXT6DJFJTAP4)
    - [Improving Deep Neural Networks Hyperparameter Tuning, Regularization and Optimization](https://www.coursera.org/account/accomplishments/certificate/JECRR78QPNL2)
    - [Neural Networks and Deep Learning](https://www.coursera.org/account/accomplishments/certificate/JN9YMWLEVLSN)
    - [Sequence Models](https://www.coursera.org/account/accomplishments/certificate/LAWZVUUY7FM5)
    - [Structuring Machine Learning Projects](https://www.coursera.org/account/accomplishments/certificate/HP3FY4KVUCCF)
    """)

with st.expander("**Datacamp**", expanded=default_page_expand):
    st.markdown("""
    - [Tableau Fundamentals Track](https://www.datacamp.com/statement-of-accomplishment/track/75d76c8576fa6ab9681b1e3654de0b0507ac9604)
    - [Analyzing Data in Tableau](https://www.datacamp.com/statement-of-accomplishment/course/0965f533174b8970b3ccfb18a717bc6b5518584b)
    - [Case Study Analyzing Customer Churn in Tableau](https://www.datacamp.com/statement-of-accomplishment/course/351a0dec5553fcae445dbc4b77c3a6dadacd9916)
    - [Creating Dashboards in Tableau](https://www.datacamp.com/statement-of-accomplishment/course/c1ee1e8761e744ef4e44c04ee5c467290101ca88)
    - [Introduction to Tableau](https://www.datacamp.com/statement-of-accomplishment/course/0a135fc3e3cff02fbfb57920a4ec37a9891e389b)
    - [Intro to statistics in Python](https://www.datacamp.com/statement-of-accomplishment/course/90495419ae27174fbbec7f9c13efecfca62e6ca0)
    - [Introduction to Data Science in Python](https://www.datacamp.com/statement-of-accomplishment/course/eb23cf332f2a4d93d4db0bc83a2a336c1ac0d25c)
    - [Time Series Analysis in Python](https://www.datacamp.com/statement-of-accomplishment/course/bd36228296ec00df215db55e08a3a3bfde614142)
    - [Introduction to Data Visualization with Seaborn](https://drive.google.com/file/d/1iC_20vpTkf6OJpfQy6BA0rCgxXqiyEN7/view?usp=drive_link)
    - [Supervised Learning with scikit-learn](https://drive.google.com/file/d/1zYEef8ll_62WHgSo32dsMzq0e9SGiaxm/view?usp=drive_link)
    - [Unsupervised Learning in Python](https://drive.google.com/file/d/1WJ1qHzbFa2rob1OImWWnBD4AMaUjhYWp/view?usp=drive_link)
    """)

with st.expander("**Kaggle**", expanded=default_page_expand):
    st.markdown("""
    - [Python](https://www.kaggle.com/learn/certification/aagalib/python)
    - [Intro to Machine Learning](https://www.kaggle.com/learn/certification/aagalib/intro-to-machine-learning)
    - [Intermediate Machine Learning](https://www.kaggle.com/learn/certification/aagalib/intermediate-machine-learning)
    """)

with st.expander("**Udacity**", expanded=default_page_expand):
    st.markdown("""
    - [AWS Machine Learning Foundations](https://drive.google.com/file/d/1sbm9DmKCZV5TfBhmWQulcgys9WorpzX1/view?usp=drive_link)
    """)
