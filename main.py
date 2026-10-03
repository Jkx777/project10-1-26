import streamlit as st
import requests
import datetime

base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

def fetch_space():
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    Base_url = base_url + "/" + str(d).replace("-", "")[2:]
    r = requests.get(f"{Base_url}")
    r.raise_for_status()
    return r.json()

d = st.date_input("Enter a date: ")
res = fetch_space(d)

st.title(res[0]["title"])
st.image(res[0]["hdurl"])
st.html(res[0]["explanation"])