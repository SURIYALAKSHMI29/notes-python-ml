import streamlit as st

# Widget's Id is assigned based on its parameters
# Changing widget's parameter changes its id, so the state

st.subheader("Value is not maintained")
min_value = st.slider("Set Min Value", 0, 50, 25)

slider_value = st.slider("Value", min_value, 100, min_value)
# when min_value is changed, the slider_value will also changed, state is not maintained
# Because -> parameters of the slider_value is changed when min_value is changed -> creates a new id


st.divider()

st.subheader("Slider Value is maintainer even when state is changed")
# Can use session_state variable to maintain its value
if "slider_value" not in st.session_state:
    st.session_state.slider_value = 25

minimum_value = st.slider("Set Minimum Value", 0, 50, 25)

st.session_state.slider_value = st.slider("Slider Value", minimum_value, 100, st.session_state.slider_value)

st.divider()


# If not rendered, internal state from the session is removed

checkbox = st.checkbox("Show Input Field")

if checkbox:
    user_input = st.text_input("Enter something: ")  # when checked again, it renders again
    # st.text_input() now resets its value to "" by default
    st.session_state.user_input = user_input
else:  # If unchecked, st.text_input() -> disappears and so its state
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input: {user_input}")
# here user_input is will get disappeared when it is checked again



# Can be solved by, binding a session_state to user input
if checkbox:
    user_input_2 = st.text_input("Enter here: ", value = st.session_state.get("user_input_2", "") )  
    st.session_state.user_input_2 = user_input_2
else:
    user_input_2 = st.session_state.get("user_input_2", "")

st.write(f"User Input 2: {user_input_2}")