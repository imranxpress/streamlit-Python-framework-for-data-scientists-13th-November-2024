import streamlit as st


def main():
    st.sidebar.title("Dashboard")
    menu = ["Home", "Dashboard", "Profile", "Settings"]
    choice = st.sidebar.selectbox("Select Menu", menu)

    if choice == "Home":
        st.title("Home Page")
        st.write("This is Home Page")
    elif choice == "Dashboard":
        st.title("Dashboard")
        st.write("This is Dashboard")
    elif choice == "Profile":
        st.title("Profile")
        st.write("This is Profile")
    elif choice == "Settings":
        st.title("Settings")
        st.write("This is Settings")
        
    cloudmenu = ["Project", "Instance", "Volume", "Network"]
    choice = st.sidebar.selectbox("Cloud", cloudmenu)
    
    if choice == "Project":
        st.title("Project")
        st.write("Create a Project")
    elif choice == "Instance":
        st.title("Instance")
        st.write("Create Instance")
    elif choice == "Volume":
        st.title("Volume")
        st.write("Create Volume")
    elif choice == "Network":
        st.title("Network")
        st.write("Create Network")

if __name__ == '__main__':
    main()
