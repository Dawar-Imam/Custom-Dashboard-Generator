import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.title("Runtime Webpage Generation")

question = st.text_input("Describe the app/web page you want to generate:")

if st.button("Make Webpage!"):
    if question:
        response = requests.post(API_URL, json={"text": question})
        st.write("Answer:", response.json()["answer"])
