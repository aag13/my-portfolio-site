import json
from datetime import datetime
import streamlit as st
import requests
import utils


utils.initialize_page_config("Asadullah Al Galib - Portfolio")
utils.set_page_header("🧑‍🎓 Education 🧑‍🎓")

with st.expander("Bachelor of Science in Computer Science and Engineering (2017)", expanded=True):
    st.markdown("""
    **University**: [BRAC University](https://www.bracu.ac.bd/)
    
    **Thesis**: [Inference of Gene Regulatory Network (GRN) From Gene Expression Data Using K-means Clustering and Entropy 
    Based Selection of Interactions](https://doi.org/10.1007/978-3-031-17181-9_9) (Presented at the International Conference 
    on Bangabandhu and Digital Bangladesh, ICBBDB 2021 )
    
    **Courses**: 
    
    Data Structures, Algorithms, Operating System, Computer Architecture, Database Systems, Compiler Design, Artificial Intelligence,
    Software Engineering, Systems Analysis and Design, Object Oriented Programming, Discrete Mathematics, 
    Mathematics I: Differential Calculus and Coordinate Geometry, Mathematics II: Integral Calculus and Differential Equations, 
    Mathematics III: Complex Variables and Laplace Transformations, Mathematics IV: Linear Algebra and Fourier Analysis,
    Elements of Statistics and Probability
    
    """)

