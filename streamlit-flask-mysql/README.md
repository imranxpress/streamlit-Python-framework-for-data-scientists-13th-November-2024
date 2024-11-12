আমরা Streamlit থেকে ইনপুট করা ডেটা MySQL ডাটাবেসে স্টোর করার পর, Flask ব্যবহার করে সেই ডেটা রিট্রিভ এবং প্রদর্শন করতে পারি। নিচে একটি উদাহরণ দেওয়া হলো যেখানে আমরা Flask অ্যাপ তৈরি করব যা MySQL ডাটাবেস থেকে ডেটা রিট্রিভ করবে।

### Step 1: Create the Flask App

1. **Create a directory structure**:
   ```
   my_project/
   ├── docker-compose.yml
   ├── init/
   │   └── init.sql
   ├── app/
   │   └── app.py
   └── flask_app/
       └── app.py
   ```

2. **Write the Flask app code in `flask_app/app.py`**:

   ```python
   from flask import Flask, jsonify
   import mysql.connector

   app = Flask(__name__)

   def get_connection():
       return mysql.connector.connect(
           host="db",
           user="root",
           password="example",
           database="streamlit_db"
       )

   @app.route('/users', methods=['GET'])
   def get_users():
       conn = get_connection()
       cursor = conn.cursor(dictionary=True)
       cursor.execute("SELECT * FROM users")
       rows = cursor.fetchall()
       conn.close()
       return jsonify(rows)

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

### Step 2: Update the `docker-compose.yml` File

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: streamlit_db
    volumes:
      - db_data:/var/lib/mysql
      - ./init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 30s
      timeout: 10s
      retries: 5

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    restart: always
    ports:
      - 8080:80
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: example
    depends_on:
      db:
        condition: service_healthy

  streamlit:
    image: python:3.9
    container_name: streamlit_app
    volumes:
      - ./app:/app
    working_dir: /app
    command: ["streamlit", "run", "app.py"]
    ports:
      - 8501:8501
    depends_on:
      db:
        condition: service_healthy
    environment:
      - PYTHONUNBUFFERED=1

  flask:
    image: python:3.9
    container_name: flask_app
    volumes:
      - ./flask_app:/flask_app
    working_dir: /flask_app
    command: ["python", "app.py"]
    ports:
      - 5000:5000
    depends_on:
      db:
        condition: service_healthy
    environment:
      - PYTHONUNBUFFERED=1

volumes:
  db_data:
```

### Step 3: Install Required Packages

1. **Create a `requirements.txt` file in both `app/` and `flask_app/` directories**:

   For `app/requirements.txt`:
   ```
   streamlit
   mysql-connector-python
   pandas
   ```

   For `flask_app/requirements.txt`:
   ```
   flask
   mysql-connector-python
   ```

2. **Update the Docker Compose file to install these dependencies**:

   Update the `streamlit` and `flask` services in `docker-compose.yml`:

   ```yaml
   streamlit:
     image: python:3.9
     container_name: streamlit_app
     volumes:
       - ./app:/app
     working_dir: /app
     command: ["sh", "-c", "pip install -r requirements.txt && streamlit run app.py"]
     ports:
       - 8501:8501
     depends_on:
       db:
         condition: service_healthy
     environment:
       - PYTHONUNBUFFERED=1

   flask:
     image: python:3.9
     container_name: flask_app
     volumes:
       - ./flask_app:/flask_app
     working_dir: /flask_app
     command: ["sh", "-c", "pip install -r requirements.txt && python app.py"]
     ports:
       - 5000:5000
     depends_on:
       db:
         condition: service_healthy
     environment:
       - PYTHONUNBUFFERED=1
   ```

### Step 4: Build and Run the Docker Containers

1. **Navigate to your project directory**:
   ```sh
   cd my_project
   ```

2. **Build and start the containers**:
   ```sh
   docker-compose up -d
   ```

3. **Access the Applications**:
   - phpMyAdmin: `http://localhost:8080`
   - Streamlit App: `http://localhost:8501`
   - Flask App: `http://localhost:5000/users`

Now, your Flask app will be able to retrieve and display the data stored in the MySQL database by the Streamlit app. If you have any further questions or need additional assistance, feel free to ask!
