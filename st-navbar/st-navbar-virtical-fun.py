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
            <a href="?page=product" onclick="setPage('product')">Product</a>
            <a href="?page=services" onclick="setPage('services')">Services</a>
            <a href="?page=about" onclick="setPage('about')">About</a>
            <a href="?page=blog" onclick="setPage('blog')">Blog</a>
        </div>
        <div class="right-menu">
            <a href="?page=signin" onclick="setPage('signin')">Sign In</a>
        </div>
    </div>
    <script>
    function setPage(page) {
        window.location.search = '?page=' + page;
    }
    </script>
    """, unsafe_allow_html=True)

# Call the navigation bar function
navigation_bar()

# Get the current page from the query parameters
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# Define the content for each page
if page == "product":
    st.title("Product Page")
    st.write("Welcome to the Product page.")
elif page == "services":
    st.title("Services Page")
    st.write("Welcome to the Services page.")
elif page == "about":
    st.title("About Page")
    st.write("Welcome to the About page.")
elif page == "blog":
    st.title("Blog Page")
    st.write("Welcome to the Blog page.")
elif page == "signin":
    st.title("Sign In Page")
    st.write("Welcome to the Sign In page.")
else:
    st.title("Home Page")
    st.write("Welcome to the Home page.")

# Add content to the page
st.write("Here is some content on the main page.")
