import streamlit as st
import requests
import datetime

base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

def fetch_space(d):
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    Base_url = base_url + "/" + str(d).replace("-", "")[2:]
    r = requests.get(f"{Base_url}")
    r.raise_for_status()
    return r.json()

d = st.date_input("Enter a date: ")
res = fetch_space(d)

st.title(res["title"])
st.image(res["hdurl"])
st.html(res["explanation"])

#=======================================================================================

base_url2 = "https://ll.thespacedevs.com/2.3.0/launches/"

def fetch_space2():
    r = requests.get(f"{base_url2}")
    r.raise_for_status()
    return r.json()

res2 = fetch_space2()
st.write(res2)