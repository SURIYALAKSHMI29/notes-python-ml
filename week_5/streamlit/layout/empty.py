import streamlit as st
import time


with st.sidebar:
    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
    
# the content will get append instead of replacing
for seconds in range(10):
    st.write(f"⏳ {seconds} seconds have passed")  # writes a new line each time
    time.sleep(1)
st.write(":material/check: 10 seconds over!")

st.divider()


# dynamic updating content 
with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed") # overwrites the single line
        time.sleep(1)
    st.write(":material/check: 10 seconds over!")
st.button("Rerun")