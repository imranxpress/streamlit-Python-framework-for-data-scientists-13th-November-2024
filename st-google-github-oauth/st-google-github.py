import streamlit as st
from streamlit_google_auth import Authenticate as GoogleAuthenticate
from streamlit_oauth import OAuth2Component
import os

st.title('Streamlit Auth Example')

# Initialize session state for authenticators if not already done
if 'google_authenticator' not in st.session_state:
    st.session_state.google_authenticator = GoogleAuthenticate(
        secret_credentials_path='google_credentials.json',
        cookie_name='google_cookie',
        cookie_key='google_secret',
        redirect_uri='http://127.0.0.1:8501',
    )

if 'github_authenticator' not in st.session_state:
    st.session_state.github_authenticator = OAuth2Component(
        client_id=os.getenv('GITHUB_CLIENT_ID'),
        client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
        authorize_endpoint='https://github.com/login/oauth/authorize',
        token_endpoint='https://github.com/login/oauth/access_token',
    )

# Display the GitHub login button
if 'github_token' not in st.session_state:
    st.write("## Login with GitHub")
    result = st.session_state.github_authenticator.authorize_button(
        "Login with GitHub", 
        redirect_uri='http://127.0.0.1:8501', 
        scope='user:email'
    )
    if result and 'token' in result:
        st.session_state.github_token = result.get('token')
        st.session_state.connected = True
        st.session_state.user_info = result.get('user_info')

# Display the Google login button
st.write("## Login with Google")
st.session_state.google_authenticator.login()

# Display user info if connected
if st.session_state.get('connected'):
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, ' + st.session_state['user_info'].get('name'))
    st.write('Your email is ' + st.session_state['user_info'].get('email'))
    if st.button('Log out'):
        st.session_state.google_authenticator.logout()
        st.session_state.github_authenticator.logout()
        st.session_state.pop('github_token', None)
        st.session_state.pop('connected', None)
        st.session_state.pop('user_info', None)
