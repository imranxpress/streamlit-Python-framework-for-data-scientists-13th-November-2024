import streamlit as st
import mysql.connector
import pandas as pd

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="172.22.0.2",
        user="sysadmin",
        password="centos@123",
        database="wordpress"
    )

# Create
def create_user(name, age, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", (name, age, email))
    conn.commit()
    conn.close()

# Read
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update
def update_user(user_id, name, age, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, age=%s, email=%s WHERE id=%s", (name, age, email, user_id))
    conn.commit()
    conn.close()

# Delete
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    conn.close()

# Streamlit UI
st.title("Simple CRUD App with Streamlit and MySQL")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add New User")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    if st.button("Add User"):
        create_user(name, age, email)
        st.success(f"User {name} added successfully")

elif choice == "Read":
    st.subheader("View Users")
    users = get_users()
    df = pd.DataFrame(users, columns=["ID", "Name", "Age", "Email"])
    st.dataframe(df)

elif choice == "Update":
    st.subheader("Update User")
    user_id = st.number_input("User ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    if st.button("Update User"):
        update_user(user_id, name, age, email)
        st.success(f"User {user_id} updated successfully")

elif choice == "Delete":
    st.subheader("Delete User")
    user_id = st.number_input("User ID", min_value=1)
    if st.button("Delete User"):
        delete_user(user_id)
        st.success(f"User {user_id} deleted successfully")
