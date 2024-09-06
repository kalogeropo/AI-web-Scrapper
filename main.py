import streamlit as st
from scrapper import scrape_website, extract_body, clean_body, create_dom_baches
st.title('AI Web Scrapper')
url = st.text_input('Enter the URL: ')

if st.button("Scrape URL"):
    st.write('Scraping the URL:', url)
    res = scrape_website(url)
    body = extract_body(res)
    clean = clean_body(body)
    print(clean)
    st.session_state.dom_content = clean
    with st.expander("Show content"):
        st.text_area("Dom Content",clean, height=600)


