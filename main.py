import streamlit as st
from scrapper import scrape_website, extract_body, clean_body, create_dom_baches
from parse_using_llms import parse_using_llms
st.title('AI Web Scrapper')
url = st.text_input('Enter the URL: ')

if st.button("Scrape URL"):
    st.write('Scraping the URL:', url)
    res = scrape_website(url)
    body = extract_body(res)
    clean = clean_body(body)
    st.session_state.dom_content = clean
    with st.expander("Show content"):
        st.text_area("Dom Content",clean, height=300)

if "dom_content"  in st.session_state:
    user_input = st.text_area("Ask your Question:")
    if st.button("Enter"):
        if user_input:
            st.write("Processing the question...")
            batches = create_dom_baches(st.session_state.dom_content)
            result =  parse_using_llms(batches,user_input)
            st.write(result)



