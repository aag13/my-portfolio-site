import json
from datetime import datetime
import streamlit as st
import requests
import utils


utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("🛠️ Skills 🛠️")

col1, col2 = st.columns(2)

with col1:
    with st.expander("Languages 🏷️", expanded=True):
        st.markdown("""
        Python, JavaScript, R, Java, Dart, SQL, Bash, YAML
        """)

with col2:
    with st.expander("Databases 📂", expanded=True):
        st.markdown("""
        PostgreSQL, MySQL, Dynamodb, RDS, Chroma, MongoDB, Redis, Apache Derby
        """)

with st.expander("Libraries & Frameworks 💻", expanded=True):
    st.markdown("""
    Django, NodeJS, BeautifulSoup, Scrapy, Selenium, Flutter, Streamlit, Airflow, PyTorch, TensorFlow, NumPy, Scikit-learn, NLTK, 
    Pandas, Seaborn, SpaCy, LangChain, Pydantic, Swing Widget Toolkit, Polymer
    """)

with st.expander("Tools & Platforms ⚙️", expanded=True):
    st.markdown("""
    **AWS** *(API Gateway, API Gateway Proxy, Lambda, Cloudwatch, OpenSearch, SAM, SQS, SNS, Cognito, IAM, S3, SES, 
    Pinpoint, Chime, VPC, KMS, ACM, Event Bridge, Nested Stack, Lambda Layers, EFS, Textract, ECR, 
    AppConfig, CodeBuild, CodeCommit, CodeDeploy, CodePipeline, Fargate, CloudFront, Glue, Lake Formation, and others)*, 
    Elasticsearch, Git, Jupyter Notebook, Celery, ActiveMQ, Jenkins, Docker, OpenAI, Tableau, Google Map
    """)
