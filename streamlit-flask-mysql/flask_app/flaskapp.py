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
