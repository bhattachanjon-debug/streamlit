import streamlit as st
import pandas as pd
import pickle as pk

with open("salary.pickle", "rb") as f:
    model = pk.load(f) 

# st.text_input("First name")
age = st.number_input("Your Age", 0, 100)
# sex = st.selectbox("Pick one", ["male", "female"])
edu = st.radio("Education Level", ["Bachelor's", "Master's", "PhD"])
# jt = st.text_input("Job Title")
exp = st.number_input("Years of Experience", 0, 50)
# st.slider("Salary", 0, 1000000)

if st.button("Submit"):
    st.success("The form is submitted successfully!")
    if edu == "Bachelor's":
        b = 1; m = 0; p = 0
    elif edu == "Master's":
        b = 0; m = 1; p = 0
    else:
        b = 0; m = 0; p = 1
    data = {"Age": [age], "Years of Experience": [exp], 
            "Bachelor's": [b], "Master's": [m], "PhD": [p]}
    df = pd.DataFrame(data)

    result = round(model.predict(df)[0],2)
    st.write(f"Predicted Salary: Rs {result}")

# st.pagination(10)

# st.segmented_control("Filter", ["Open", "Closed"])
# st.toggle("Enable")

# st.multiselect("Buy", ["milk", "apples", "potatoes"])

# st.select_slider("Pick a size", ["S", "M", "L"])




# st.text_area("Text to translate")
# st.date_input("Your birthday")
# st.datetime_input("Event date and time")
# st.time_input("Meeting time")
# st.file_uploader("Upload a CSV")
# st.audio_input("Record a voice message")
# st.camera_input("Take a picture")
# st.color_picker("Pick a color")
