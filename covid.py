import streamlit as st
import pandas as pd
import pickle as pk

with open("Covid_Classification.pickle", "rb") as f:
    model = pk.load(f) 

st.title("Covid Prediction")

Cough_symptoms = st.selectbox("Cough Symptoms = ", [True, False])
Fever = st.selectbox("Fever = ", [True, False])
Sore_throat = st.selectbox("Sore_throat = ", [True, False])
Shortness_of_breath = st.selectbox("Shortness_of_breath = ", [True, False])
Headache = st.selectbox("Headache = ", [True, False])
Known_contact = st.selectbox("Known_contact = ", ["Abroad", "Contact with confirmed", 
                                                  "Other"])

if Known_contact == "Abroad":
    Known_contact = 0
elif Known_contact == "Contact with confirmed":
    Known_contact = 1
else: 
    Known_contact = 2

if st.button("Predict"):
    st.success("The form is submitted successfully!")
    data = {"Cough_symptoms":[Cough_symptoms],"Fever":[Fever],"Sore_throat":[Sore_throat],
            "Shortness_of_breath":[Shortness_of_breath],"Headache":[Headache],
            "Known_contact":[Known_contact]}
    
    df = pd.DataFrame(data)
    result = model.predict(df)
    st.write(f"Predicted Result: {result}")