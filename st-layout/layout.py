import streamlit as st
st.title("Create a Project")

pname,ppass = st.columns(2)

pname.text_input("Project Name")
ppass.text_input("Password")