import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Create a horizontal navigation bar
def navigation_bar():
    st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #333;
        padding: 10px;
        width: 100%;
    }
    .navbar .left-menu {
        display: flex;
        align-items: center;
    }
    .navbar .logo img {
        height: 40px;
        margin-right: 20px;
    }
    .navbar a {
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        text-align: center;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    .navbar .right-menu {
        display: flex;
        align-items: center;
    }
    </style>
    <div class="navbar">
        <div class="left-menu">
            <div class="logo"><img src="pclogo.png" alt="Company Logo"></div>
            <a href="#product">Product</a>
            <a href="#services">Services</a>
            <a href="#about">About</a>
            <a href="#blog">Blog</a>
        </div>
        <div class="right-menu">
            <a href="#signin">Sign In</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Call the navigation bar function
navigation_bar()

# Add content to the page
st.title("Welcome to Our Company")
st.write("Here is some content on the main page.")
