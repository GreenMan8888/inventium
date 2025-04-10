import streamlit as st
from backend import app

st.title("Inventium")

if st.button("Say Hello"):
    st.write(app.hello())
