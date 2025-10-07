import streamlit as st
import time

st.header("Layout")
st.divider()

# Sidebar
sidebar = st.sidebar
sidebar.title("View Pokemons")
sidebar.subheader("Pick whatever you want")

# Tabs
tabs = sidebar.tabs(["Pikachu", "Greninja"])
with tabs[0]:
    st.write("You are on Pikachu's side")
    st.image("..\static\pikachu.png")
with tabs[1]:
    st.write("You are on Greninja's side")
    st.image("..\static\greninja.png")

# Container
st.subheader("Container")
with st.container(horizontal=True, border=True, horizontal_alignment="distribute"):
    # elements are placed side-by-side
    st.write("Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu")
    st.write("Bulbasur, Everthing is wrong and you are right")
    st.write("Greninja")  
    st.write("Charmander")
    st.write("Squirtle")
    st.write("Charmeleon")

with st.container(border=True, height=150):
    # separate line for each write()
    st.write("Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu Pikachu")
    st.write("Bulbasur, Everthing is wrong and you are right")
    st.write("Greninja")
    st.write("Charmander")
    st.write("Squirtle")
    st.write("Charmeleon")
st.divider()

# Columns
st.subheader("Columns")
cols = st.columns(2)
with cols[0]:
    st.subheader("Column 1")
    st.caption("This is column 1 side")
    st.image(r"..\static\ash_greninja.jpg")
    st.write("The scene where ash and greninja becomes one and acts together")
    
with cols[1]:
    st.subheader("Column 2")
    st.caption("This is column 2 side")
    st.image("..\static\pika_ash.jpg")
    st.write("Ash and pikachu first meeting")
    
st.divider()

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index = 1
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")
