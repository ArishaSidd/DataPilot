import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

st.set_page_config(page_title="DataPilot - Introduction")

# Load environment variables
load_dotenv()

#st.title("🧠 Welcome to DataPilot")

st.markdown("""
    # 🧠 Welcome to DataPilot — Your Intelligent Data Companion

    This interactive tool is designed to help you **analyze, visualize, and understand your data** with the support of AI.  
    Whether you're exploring a dataset or building a machine learning model, DataPilot guides you at every step.

    ### 🔍 Features
    - 📂 Upload datasets and explore them easily
    - 📊 Interactive visualizations with AI explanations
    - 🤖 Train ML models with guided code
    - 💬 Built-in chatbot to explain code and concepts

    > Dataset used :  [Link](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers) Download and Upload
    """)

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df
    st.success("✅ Dataset uploaded successfully!")

if st.button("Go to Data Exploration →"):
    st.switch_page("pages/1_Data_Exploration.py")
