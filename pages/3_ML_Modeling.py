import streamlit as st
import joblib
import pandas as pd
import xgboost as xgb
from matplotlib import pyplot as plt

st.set_page_config(page_title="DataPilot - ML Modeling")

st.title("🧠 ML Modeling")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first from the Home page.")
    st.stop()

st.subheader("Customer Attrition Prediction")


with st.form("Customer Details"):
    Age = st.number_input("Customer's Age",min_value=28,max_value=70, step=1, format="%d")
    Gender = st.selectbox("Gender",["M","F"])
    Dependent_count = st.number_input("Customer's Dependent Count",min_value=0,max_value=5, step=1, format="%d")
    Education_Level = st.selectbox("Education",['High School', 'Graduate', 'Uneducated', 'Unknown', 'College','Post-Graduate', 'Doctorate'])
    Marital_Status = st.selectbox("Marital Status",["Married","Single","Divorced","Unknown"])
    Income_Category = st.selectbox("Income Level",['$60K - $80K', 'Less than $40K', '$80K - $120K', '$40K - $60K','$120K +', 'Unknown'])
    Card_Category = st.selectbox("Card Category",['Blue', 'Gold', 'Silver', 'Platinum'])
    Months_on_book = st.number_input("Period of Relationship",min_value=13,max_value=56, step=1, format="%d")
    Total_Relationship_Count = st.number_input("Number of products held",min_value=1,max_value=6, step=1, format="%d")
    Months_Inactive_12_mon = st.number_input("Months inactive last yr",min_value=0,max_value=6, step=1, format="%d")
    Contacts_Count_12_mon = st.number_input("People contacted last yr",min_value=0,max_value=6, step=1, format="%d")
    Credit_Limit = st.number_input("Credit Limit",min_value=1500.0,max_value=34000.0)
    Total_Revolving_Bal = st.number_input("Total Revolving Balance",min_value=0,max_value=2500,step=1, format="%d")
    Avg_Open_To_Buy = st.number_input("Average Open to Buy",min_value=0.0,max_value=34000.0)
    Total_Amt_Chng_Q4_Q1 = st.number_input("Total Trans-Amount change Q1-Q4",min_value=0.0,max_value=3.3)
    Total_Trans_Amt = st.number_input("Total Transaction Amount",min_value=510,max_value=18000,step=1, format="%d")
    Total_Trans_Ct = st.number_input("Total Transaction Count",min_value=10,max_value=135,step=1, format="%d")
    Total_Ct_Chng_Q4_Q1 = st.number_input("Total Trans-Count change Q1-Q4",min_value=0.0,max_value=3.7)
    Avg_Utilization_Ratio = st.number_input("Age Utilization Ratio",min_value=0.0,max_value=0.99)

    submitted = st.form_submit_button("Predict")

if submitted:
   
    preprocessor = joblib.load("model/preprocessor_DataPilot.pkl")
    model = joblib.load("model/balanced_random_forest_model.pkl")


    input_data = pd.DataFrame([{
        'Customer_Age': Age,
        'Gender': Gender,
        'Dependent_count': Dependent_count,
        'Education_Level': Education_Level,
        'Marital_Status': Marital_Status,
        'Income_Category': Income_Category,
        'Card_Category': Card_Category,
        'Months_on_book': Months_on_book,
        'Total_Relationship_Count': Total_Relationship_Count,
        'Months_Inactive_12_mon': Months_Inactive_12_mon,
        'Contacts_Count_12_mon': Contacts_Count_12_mon,
        'Credit_Limit': Credit_Limit,
        'Total_Revolving_Bal': Total_Revolving_Bal,
        'Avg_Open_To_Buy': Avg_Open_To_Buy,
        'Total_Amt_Chng_Q4_Q1': Total_Amt_Chng_Q4_Q1,
        'Total_Trans_Amt': Total_Trans_Amt,
        'Total_Trans_Ct': Total_Trans_Ct,
        'Total_Ct_Chng_Q4_Q1': Total_Ct_Chng_Q4_Q1,
        'Avg_Utilization_Ratio': Avg_Utilization_Ratio
    }])

    # Apply preprocessing
    try:
        X_processed = preprocessor.transform(input_data)
        prediction = model.predict(X_processed)[0]
        result = "Attrited Customer" if prediction == 0 else "Existing Customer"
        if(result == "Existing Customer"):
          st.success(f"🧠 Prediction: **{result}**")
        else:
            st.error(f"🧠 Prediction: **{result}**")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

    
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot feature importance for Balanced Random Forest
    st.markdown("> These column names are a result of preprocessing.")
    
    importances = model.feature_importances_
    feature_names = model.feature_names_in_
    
    feat_imp_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    
    ax.barh(feat_imp_df['Feature'], feat_imp_df['Importance'])
    ax.invert_yaxis()
    ax.set_xlabel("Feature Importance (Gini-based)")
    ax.set_ylabel("Feature")
    ax.set_title("Feature Importance - Balanced Random Forest")
    
    st.pyplot(fig)

    
st.image("images/imp_features.png")

