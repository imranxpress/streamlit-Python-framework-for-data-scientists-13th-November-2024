import streamlit as st
from streamlit_google_auth import Authenticate

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Function to render the header
def render_header():
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    with col1:
        st.image('pclogo.png', width=100)
    with col2:
        st.button('Home')
    with col3:
        st.button('About')
    with col4:
        st.text_input('Search')
    with col5:
        if st.session_state['connected']:
            st.image(st.session_state['user_info'].get('picture'), width=50)
            st.write(st.session_state['user_info'].get('name'))
            if st.button('Log out'):
                st.session_state["authenticator"].logout()
        else:
            st.button('Sign In')

# Function to render the authenticated header
def render_authenticated_header():
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    with col1:
        st.image('pclogo.png', width=100)
    with col2:
        st.button('Dashboard')
    with col3:
        st.button('Profile')
    with col4:
        st.text_input('Search')
    with col5:
        st.image(st.session_state['user_info'].get('picture'), width=50)
        st.write(st.session_state['user_info'].get('name'))
        if st.button('Log out'):
            st.session_state["authenticator"].logout()

# Authentication setup
if 'connected' not in st.session_state:
    authenticator = Authenticate(
        secret_credentials_path='google_credentials.json',
        cookie_name='my_cookie_name',
        cookie_key='this_is_secret',
        redirect_uri='http://127.0.0.1:8501',
    )
    st.session_state["authenticator"] = authenticator
    st.session_state['connected'] = False
    st.session_state['user_info'] = {}

# Catch the login event
st.session_state["authenticator"].check_authentification()

# Create the login button
st.session_state["authenticator"].login()

# Render the appropriate header based on authentication status
if st.session_state['connected']:
    # Assuming the authenticator sets user_info in session_state
    user_info = st.session_state.get('user_info', {})
    render_authenticated_header()
else:
    render_header()

# Main content
st.write("Welcome to the application!")
