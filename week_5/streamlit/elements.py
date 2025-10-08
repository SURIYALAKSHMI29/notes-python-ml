import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# TEXT ELEMENTS

st.title("Pokemon")
st.header("Ash and his Pokemons")
st.subheader("A day Ash got his first pokemon - pikachu")
st.markdown("_Pikachu_ - a pokemon no one dared to pick")
st.caption("But became friend with Ash Ketchum")

code_ex = """
def greet(pokemon):
    return f"Hello {pokemon}. I am Ash Ketchum from palet town"
"""

st.image("static/pokemon-first-episode.jpg", caption="Ash and Pikachu first meeting")
st.divider()

st.html("<p> Sample greet() code<p>")
st.code(code_ex, language="python")

st.divider()


# DATA ELEMENTS
st.header("Data Elements")

data = pd.DataFrame(
    {
        "Name": ("Suriya", "Sahira", "Arav", "Raji", "Karthiga"),
        "Class": ("IV yr", "NA", "LKG", "PG", "Work"),
    }
)

st.subheader("Data Frame")
st.dataframe(data)

st.subheader("Editable Data Frame")
editable_data = st.data_editor(data)
print("Updated data:\n", editable_data)

st.subheader("Static Data Frame")
st.table(data)

st.divider()


# CHART ELEMENTS
st.header("Chart elements")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["c1", "c2", "c3"])
print(chart_data)  # mean = 0, sd = 1

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter Chart")
st.scatter_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

