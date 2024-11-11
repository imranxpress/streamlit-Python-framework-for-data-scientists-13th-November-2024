import streamlit as st
from streamlit_google_auth import Authenticate

# Set page configuration to wide mode
st.set_page_config(layout="wide", page_title="Professional App", page_icon=":rocket:")

# Custom CSS for styling
st.markdown("""
    <style>
    .header {
        background-color: #f8f9fa;
        padding: 10px 0;
        border-bottom: 1px solid #e0e0e0;
    }
    .header img {
        max-width: 100px;
    }
    .header .menu {
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .header .menu button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .header .menu button:hover {
        background-color: #0056b3;
    }
    .header .user-menu {
        display: flex;
        align-items: center;
    }
    .header .user-menu img {
        border-radius: 50%;
        margin-right: 10px;
    }
    .search-bar input {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to render the header
def render_header():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    with col1:
        st.image('pclogo.png')
    with col2:
        if st.button('Home'):
            st.session_state['page'] = 'home'
    with col3:
        if st.button('About'):
            st.session_state['page'] = 'about'
    with col4:
        st.markdown('<div class="search-bar"><input type="text" placeholder="Search..."></div>', unsafe_allow_html=True)
    with col5:
        if st.session_state['connected']:
            with st.expander("User Menu"):
                st.image(st.session_state['user_info'].get('picture'), width=50)
                st.write(st.session_state['user_info'].get('name'))
                if st.button('Log out'):
                    st.session_state["authenticator"].logout()
        else:
            if st.button('Sign In'):
                st.session_state['page'] = 'signin'
    st.markdown('</div>', unsafe_allow_html=True)

# Function to render the authenticated header
def render_authenticated_header():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    with col1:
        st.image('pclogo.png')
    with col2:
        if st.button('Dashboard'):
            st.session_state['page'] = 'dashboard'
    with col3:
        if st.button('Profile'):
            st.session_state['page'] = 'profile'
    with col4:
        st.markdown('<div class="search-bar"><input type="text" placeholder="Search..."></div>', unsafe_allow_html=True)
    with col5:
        with st.expander("User Menu"):
            st.image(st.session_state['user_info'].get('picture'), width=50)
            st.write(st.session_state['user_info'].get('name'))
            if st.button('Log out'):
                st.session_state["authenticator"].logout()
    st.markdown('</div>', unsafe_allow_html=True)

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
    st.session_state['page'] = 'home'

# Catch the login event
st.session_state["authenticator"].check_authentification()

# Create the login button
st.session_state["authenticator"].login()

# Render the appropriate header based on authentication status
if st.session_state['connected']:
    user_info = st.session_state.get('user_info', {})
    render_authenticated_header()
else:
    render_header()

# Main content based on the current page
if st.session_state['page'] == 'home':
    st.write("Welcome to the home page!")
elif st.session_state['page'] == 'about':
    st.write("About us page content goes here.")
elif st.session_state['page'] == 'signin':
    st.write("Please sign in using the button below.")
    st.session_state["authenticator"].login()
elif st.session_state['page'] == 'dashboard':
    st.write("Welcome to your dashboard!")
elif st.session_state['page'] == 'profile':
    st.write("This is your profile page.")
    st.image(user_info.get('picture'), width=50)
    st.write(f'User Name: {user_info.get("name", "")}')
    st.write(f'Email: {user_info.get("email", "")}')
