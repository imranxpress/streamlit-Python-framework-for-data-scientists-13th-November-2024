# Working With MySQL and Streamlit  

## Try this Codes on Docker
```
git clone https://github.com/SumonPaul18/streamlit.git
cd streamlit/streamlit-mysql
docker compose up -d
```
## Output this Codes 
```
docker ps 
```
---
## Try this Codes on Host
Here are the steps to connect a MySQL database to a Streamlit app and perform simple CRUD (Create, Read, Update, Delete) operations:

### Step 1: Set Up Your Environment
1. **Install Required Packages**:
   Make sure you have `streamlit`, `mysql-connector-python`, and `pandas` installed. You can install them using pip:
   ```sh
   pip install streamlit mysql-connector-python pandas
   ```

### Step 2: Create a MySQL Database and Table
1. **Create a Database**:
   Use phpMyAdmin or MySQL command line to create a database and a table. For example:
   ```sql
   CREATE DATABASE streamlit_db;
   USE streamlit_db;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       age INT,
       email VARCHAR(100)
   );
   ```

### Step 3: Write the Streamlit App
1. **Connect to MySQL and Perform CRUD Operations**:
   Create a Python script for your Streamlit app. Here's an example:

   ```python
   import streamlit as st
   import mysql.connector
   import pandas as pd

   # MySQL connection
   def get_connection():
       return mysql.connector.connect(
           host="localhost",
           user="root",
           password="example",
           database="streamlit_db"
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
   ```

### Step 4: Run Your Streamlit App
1. Save the script as `app.py`.
2. Run the Streamlit app using the following command:
   ```sh
   streamlit run app.py
   ```

This will start the Streamlit app, and you can access it in your browser. You can now perform CRUD operations on your MySQL database through the Streamlit interface.

