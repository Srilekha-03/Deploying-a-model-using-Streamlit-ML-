import streamlit as st
import numpy as np 
import pickle
import pandas as pd


pickle_in = open(r"C:\Users\srile\Downloads\classifier (3).pkl", "rb")
rf_model = pickle.load(pickle_in)

def Welcome():
    return "Welcome All"

def predict_credit_card_risk(Gender, Has_a_car, Has_a_property, Children_count, Income, Employment_status, Education_level, Marital_status, Dwelling, Has_a_mobile_phone, Job_title, Family_member_count):
    # Function implementation

    # Function implementation

    prediction = rf_model.predict([[Gender, Has_a_car, Has_a_property, Children_count, Income, Employment_status, Education_level, Marital_status, Dwelling, Has_a_mobile_phone, Job_title, Family_member_count]])
    print(prediction)
    return prediction

    # Function implementation
def main():
    st.title("CREDIT CARD PREDICTION DATASET DEPLOYED MODEL")
    html_temp="""
    <div style="background-color:tomato;padding:12px">
    <h2 style="coor:white;text-align:center;">Streamlit Credit card Predictor</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.text_input("Gender","Enter here")
    Has_a_car = st.text_input("Has_a_car","Enter here")
    Has_a_property = st.text_input("Has_a_property","Enter here")
    Children_count = st.text_input("children_count","Enter here")
    Income= st.text_input("Income","Enter here")
    Employment_status = st.text_input("Employment_status","Enter here")
    Education_level = st.text_input("Education_level","Enter here")
    Marital_status = st.text_input("Marital_status","Enter here")
    Dwelling = st.text_input("Dwelling","Enter here")
    Has_a_mobile_phone = st.text_input("Has_a_mobile_phone","Enter here")
    Job_title = st.text_input("Job_title","Enter here")
    Family_member_count = st.text_input("Family_member_count","Enter here")
    result=""
    if st.button("Predict"):
        result=predict_credit_card_risk(Gender, Has_a_car, Has_a_property, Children_count, Income, Employment_status, Education_level, Marital_status, Dwelling, Has_a_mobile_phone, Job_title, Family_member_count)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built w Streamlit")
if __name__=='__main__':
    main()