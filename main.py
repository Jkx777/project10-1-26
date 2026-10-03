import streamlit as st
import requests
import datetime

base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"

def fetch_space():
    d = st.date_input("Enter a date: ")
    st.write(str(d).replace("-", ""))
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    r = requests.get(f"{base_url + str(d).replace("-", "")}")
    r.raise_for_status()
    return r.json()

res = fetch_space()
st.title(res[0]["title"])
st.image(res[0]["hdurl"])
st.html(res[0]["explanation"])