import streamlit as st

st.title("Pokemon")
st.header("Ash and his Pokemons")
st.subheader("A day Ash got his first pokemon - pikachu")
st.markdown("_Pikachu_ - a pokemon no one dared to pick")
st.caption("But became friend with Ash Ketchum")

st.image("static\pika_ash.jpg", caption="Ash and Pikachu first meeting")
st.divider()   # hr tag

code_ex = """
def greet(pokemon):
    return f"Hello {pokemon}. I am Ash Ketchum from palet town"
"""

st.html("<p> Sample greet() code<p>")
st.code(code_ex, language="python")