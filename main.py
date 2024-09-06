import streamlit as st

st.title('AI Web Scrapper')
url = st.text_input('Enter the URL: ')

if st.button("Scrape URL"):
    st.write('Scraping the URL:', url)
