import streamlit as st
import requests

api="jyvQWPPRWkTDWfOelzcugKOeWdxsNpl4ombucdRY"
url=f"https://api.nasa.gov/planetary/apod?api_key={api}"

response=requests.get(url)
content=response.json()

img_url=content["url"]
text=content["explanation"]
title=content["title"]

img=requests.get(img_url)
with open("image.jpg", "wb") as file:
    file.write(img.content)

st.header(title)
st.image("image.jpg")
st.write(text)
