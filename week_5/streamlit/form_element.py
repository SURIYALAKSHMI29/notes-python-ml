import streamlit as st
from datetime import datetime

# Initialize with None
student_data = {
    "name": None,
    "year": None,
    "dob": None,
    "gender": None,
    "address": None,
}

min_date = datetime(1900, 1, 1)
max_date = datetime.now()

with st.form(key="student_data_form"):
    student_data["name"] = st.text_input("Your name: ")
    student_data["year"] = st.selectbox("Year: ", ["I", "II", "III", "IV"])
    student_data["dob"] = st.date_input("Date of Birth: ", min_value = min_date, max_value= max_date)
    student_data["gender"] = st.selectbox("Gender: ", ["Male", "Female", "Other"])
    student_data["address"] = st.text_area("Address: ")
    
    if(student_data["dob"]):
        age = max_date.year - student_data["dob"].year
        st.write(f"You are {age} old") 
        # get updated only after submitting, because we are not rendering only when submit is clicked
        # can use session state
    submit_button = st.form_submit_button()
    
if submit_button:   # after submitting it reruns the file
    if not all(student_data.values()):
        st.warning("Please fill all the fields and try submitting again!")
    else:
        st.balloons()
        st.write("### Info")
        for (key, value) in student_data.items():
            st.write(f"{key.capitalize()}: {value}")
