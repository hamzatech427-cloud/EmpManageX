from flask import Flask, request, jsonify, session, send_from_directory, redirect, url_for
from flask_cors import CORS
import mysql.connector
from datetime import timedelta
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate a secure secret key
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

CORS(app, supports_credentials=True)


ADMIN_USERNAME = "admin"  
ADMIN_PASSWORD = "admin123"  

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # Write your user here 
        password="YOUR_PASSWORD_HERE",  # Write your password here
        database="companydb"
    )

# Initialize database tables
def init_db():
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        # Create employee table if not exists
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                Empid INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                department VARCHAR(50) NOT NULL,
                salary DECIMAL(10, 2) NOT NULL
            )
        """)
        
        mydb.commit()
        mycursor.close()
        mydb.close()
    

# HTML PAGE ROUTES

# Root route - redirects to login or dashboard based on authentication
@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login_page'))

# Login page
@app.route('/login')
def login_page():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('dashboard'))
    return send_from_directory('.', 'login.html')

# Dashboard page (protected)
@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login_page'))
    return send_from_directory('.', 'dashboard.html')

# AUTHENTICATION APIs

# Login user (hardcoded admin only)
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        # Check against hardcoded admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            # Create session
            session.permanent = True
            session['user_id'] = 1
            session['username'] = ADMIN_USERNAME
            session['logged_in'] = True
            
            return jsonify({
                "message": "Login successful",
                "user": {
                    "id": 1,
                    "username": ADMIN_USERNAME
                }
            }), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Logout user
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

# Check if user is logged in
@app.route('/api/check-auth', methods=['GET'])
def check_auth():
    if 'logged_in' in session and session['logged_in']:
        return jsonify({
            "authenticated": True,
            "user": {
                "id": session.get('user_id'),
                "username": session.get('username')
            }
        }), 200
    else:
        return jsonify({"authenticated": False}), 401

# Middleware to check authentication
def login_required(f):
    def wrapper(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

# EMPLOYEE CRUD APIs (Protected)

# CREATE - Add new employee
@app.route('/api/employee', methods=['POST'])
@login_required
def create_employee():
    try:
        data = request.json
        name = data.get('name')
        department = data.get('department')
        salary = data.get('salary')
        
        if not name or not department or not salary:
            return jsonify({"error": "All fields (name, department, salary) are required"}), 400
        
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        insert_query = "INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)"
        mycursor.execute(insert_query, (name, department, salary))
        mydb.commit()
        
        new_id = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        
        return jsonify({
            "message": "Employee created successfully",
            "employee_id": new_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ - Get all employees
@app.route('/api/employees', methods=['GET'])
@login_required
def get_employees():
    try:
        mydb = get_db_connection()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM employee ORDER BY Empid")
        employees = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return jsonify(employees), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ - Get single employee by ID
@app.route('/api/employee/<int:emp_id>', methods=['GET'])
@login_required
def get_employee(emp_id):
    try:
        mydb = get_db_connection()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM employee WHERE Empid = %s", (emp_id,))
        employee = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        
        if employee:
            return jsonify(employee), 200
        else:
            return jsonify({"error": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# UPDATE - Update employee
@app.route('/api/employee/<int:emp_id>', methods=['PUT'])
@login_required
def update_employee(emp_id):
    try:
        data = request.json
        name = data.get('name')
        department = data.get('department')
        salary = data.get('salary')
        
        if not name or not department or not salary:
            return jsonify({"error": "All fields (name, department, salary) are required"}), 400
        
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        update_query = "UPDATE employee SET name = %s, department = %s, salary = %s WHERE Empid = %s"
        mycursor.execute(update_query, (name, department, salary, emp_id))
        mydb.commit()
        
        if mycursor.rowcount == 0:
            mycursor.close()
            mydb.close()
            return jsonify({"error": "Employee not found"}), 404
        
        mycursor.close()
        mydb.close()
        
        return jsonify({"message": "Employee updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE - Delete employee
@app.route('/api/employee/<int:emp_id>', methods=['DELETE'])
@login_required
def delete_employee(emp_id):
    try:
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        delete_query = "DELETE FROM employee WHERE Empid = %s"
        mycursor.execute(delete_query, (emp_id,))
        mydb.commit()
        
        if mycursor.rowcount == 0:
            mycursor.close()
            mydb.close()
            return jsonify({"error": "Employee not found"}), 404
        
        mycursor.close()
        mydb.close()
        
        return jsonify({"message": "Employee deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()  # Initialize database tables
    app.run(debug=True, port=5000)