import streamlit as st

st.title("Callback")

# the app reruns top to bottom on every user interaction

st.subheader("Without callback")
if "count" not in st.session_state:
    st.session_state.count = 0

st.write("Count:", st.session_state.count)

if st.button("Increase"):
    st.session_state.count += 1

if st.button("Reset"):
    st.session_state.count = 0

# After clicking Increase button twice -> the count value will become as 1
# Because, Clicking a button triggers a rerun of the entire script
# This time, the button value is True so it updates the counter value 
# write is above the if statement, so it shows the prev value

st.divider()

st.subheader("With callback")
def increase():
    st.session_state.count_value += 1

def reset():
    st.session_state.count_value = 0
    
if "count_value" not in st.session_state:
    st.session_state.count_value = 0

st.write("count_value:", st.session_state.count_value)

st.button("Increase count_value", on_click=increase)
st.button("Reset count_value", on_click=reset)
