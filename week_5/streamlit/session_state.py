import streamlit as st

st.header("Session State")

st.subheader("Without Session state")
counter = 0

# will never get updated
# When the button is clicked, the file reruns -> set counter value back to 0
st.write(f"Counter value: {counter}")

if st.button("Increment by 1"):
    counter += 1
    st.write(f"Counter incremented to: {counter}")
else:
    st.write(f"Counter stays at: {counter}")
    
st.divider()

st.subheader("With Session state")
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter+=1
    st.write(f"Counter value incremented: {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
    
st.write(f"Counter value: {st.session_state.counter}")    