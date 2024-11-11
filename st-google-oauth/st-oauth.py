import streamlit as st
from streamlit_google_auth import Authenticate

st.title('Streamlit Google Auth Example')

if 'connected' not in st.session_state:
    authenticator = Authenticate(
        secret_credentials_path = 'google_credentials.json',
        cookie_name='my_cookie_name',
        cookie_key='this_is_secret',
        redirect_uri = 'http://127.0.0.1:8501',
    )
    st.session_state["authenticator"] = authenticator

# Catch the login event
st.session_state["authenticator"].check_authentification()

# Create the login button
st.session_state["authenticator"].login()

if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, '+ st.session_state['user_info'].get('name'))
    st.write('Your email is '+ st.session_state['user_info'].get('email'))
    if st.button('Log out'):
        st.session_state["authenticator"].logout()
        
userimage = st.session_state['user_info'].get('picture')
username = st.session_state['user_info'].get('name')
#useremail=st.session_state['user_info'].get('email')

st.write(f'User Name: {username}')
st.image({userimage})