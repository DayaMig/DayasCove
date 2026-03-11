import streamlit as st

st.title("Mig Russel Aldaya")
st.write("Welcome here gang")

name = st.text_input("Enter yo name")
if name:
    st.write("Hello,", name)