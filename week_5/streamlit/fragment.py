import streamlit as st

st.title("My Awesome App")

counter = 0

@st.fragment()
def toggle_and_text():
    global counter
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")
    st.write(f"Counter value: {counter}")  # 0
    counter+=1

@st.fragment()
def filter_and_file():
    global counter
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")
    st.write(f"Counter value: {counter}")   # 1
    counter+=1


toggle_and_text()
st.divider()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
st.divider()

filter_and_file()