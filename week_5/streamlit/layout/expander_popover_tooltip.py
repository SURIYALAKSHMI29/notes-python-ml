import streamlit as st

with st.popover("Filter Items"):
    red = st.checkbox("Show Red items")
    blue = st.checkbox("Show Blue items")
    green = st.checkbox("Show Green items")

if red:
    st.write(":red[Red Item]")
if blue:
    st.write(":blue[Blue Item]")
if green:
    st.write(":green[Green Item]")
    

with st.expander("View Details"):
    st.markdown("""
        A simple popover, that allows you to pick the color contents you want.
        And this is a _expander_        
        """)
    st.button("Hover me", help="Tooltip is shown right?! ")