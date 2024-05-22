import json
from datetime import datetime
import streamlit as st
import requests
import utils

utils.initialize_page_config("Asadullah Al Galib")
utils.set_page_header("Papers")

default_page_expand = False

with st.expander(
        "Inference of Gene Regulatory Network (GRN) From Gene Expression Data Using K-means Clustering and Entropy Based Selection of Interactions *(ICBBDB, 2021)*",
        expanded=default_page_expand):
    st.markdown("""
    *This paper was presented at the International Conference on Bangabandhu and Digital Bangladesh, ICBBDB 2021.*
    
    **Link**: https://doi.org/10.1007/978-3-031-17181-9_9
    
    **Tech**: R
    """)


with st.expander(
        "Large Scale Web Crawling and Distributed Search Engines: Techniques, Challenges, Current Trends, and Future Prospects *(ICOCI, 2023)*",
        expanded=default_page_expand):
    st.markdown("""
    *This paper was presented at the International Conference on Computing and Informatics, ICOCI 2023.*

    **Link**: https://doi.org/10.1007/978-981-99-9589-9_2

    **Tech**: Python, Beautiful Soup, AsyncIO
    """)

with st.expander(
        "Genre Classification: A Machine Learning Based Comparative Study of Classical Bengali Literature *(ICCIT, 2023)*",
        expanded=default_page_expand):
    st.markdown("""
    *This paper was presented at the 26th International Conference on Computer and Information Technology, ICCIT 2023*

    **Link**: https://doi.org/10.1109/ICCIT60459.2023.10441603

    **Tech**: Python, Scikit-learn, Seaborn, TensorFlow
    """)

