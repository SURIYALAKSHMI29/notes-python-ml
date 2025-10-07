import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.header("Cache")

st.subheader("Using cache_data")


@st.cache_data(ttl=30, show_spinner="Loading function with cache_data decorator")  # 30 sec; customized the spinner text
def load_data():
    time.sleep(3)
    return pd.DataFrame({
        "Name": ["Pikachu", "Greninja", "Charmander"],
        "Type": ["Electric", "Water", "Fire"]
    })  # always returns a new copy

cols_data = st.columns(2)

with cols_data[0]:
    start = datetime.now()
    data = load_data()
    st.write(data)
    end = datetime.now()
    st.write(f"Time taken by first call: {end - start}")
    # Time taken by first call: 0:00:03.010400

    data["Name"] = data["Name"].str.upper()  # won't modify the content in cached data
    st.caption("Modifying the data: Changing names into UpperCase")

with cols_data[1]:
    start2 = datetime.now()
    st.write(load_data())
    end2 = datetime.now()
    st.write(f"Time taken by second call: {end2 - start2}")
    # Time taken by second call: 0:00:00.003850

st.divider()


st.subheader("Using cache_resource")

cols_resource = st.columns(2)
@st.cache_resource(ttl=30)  # 30 sec
def load_model():
    time.sleep(5)
    return {"model": "ML model"}
    
with cols_resource[0]:
    start = datetime.now()
    model = load_model()
    st.write(model)
    end = datetime.now()
    st.write(f"Time taken by first call: {end - start}")
    # Time taken by first call: 0:00:05.005050
    
    model["version"] = "1.0" # gets modified in cached data
    st.caption("Modifying the data: adding version")

with cols_resource[1]:
    start2 = datetime.now()
    st.write(load_model())
    end2 = datetime.now()
    st.write(f"Time taken by second call: {end2 - start2}")
    # Time taken by second call: 0:00:00.002023