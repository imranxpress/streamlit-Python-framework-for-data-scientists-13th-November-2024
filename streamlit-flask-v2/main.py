import requests
import streamlit as st

st.title("Input your Query")
selector = st.text_area(label="Input Query", value="", height=None, max_chars=None, key=None, help=None, on_change=None,
                        args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="hidden")
query_text_sql = selector

if st.button("Search", type='primary'):
    data = requests.get("http://localhost:1111/check_api", params={"query": query_text_sql}).json()
    output_query = data["response"]
    st.header("Query Response")
    st.write(output_query)
