import streamlit as st


st.title("Take a Your Cloud Platform")
st.subheader("Given a Name for Cloud")


with st.form("oporject", clear_on_submit=True):
	name = st.text_input("Given a Name for Cloud")
	password = st.text_input("Password")
	
	submit = st.form_submit_button("Create")