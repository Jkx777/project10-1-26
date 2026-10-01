import streamlit as st
import requests

base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key=DEMO_KEY"

def fetch_space():
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    r = requests.get(f"{base_url}")
    r.raise_for_status()
    return r.json()

res = fetch_space()
st.title(res[0]["title"])
st.image(res[0]["hdurl"])