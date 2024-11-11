import streamlit as st


st.title("Create a Project")

pname,ppass = st.columns(2)

pname.text_input("Project Name")
ppass.text_input("Password")

col1,col2,col3 = st.columns(3)

col1.text_input("A")
col2.text_input("B")
col3.text_input("C")