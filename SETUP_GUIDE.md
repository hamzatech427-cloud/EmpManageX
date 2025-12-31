# 🚀 Flask Employee Management System - Complete Setup Guide

## 📋 Table of Contents
1. Prerequisites
2. Installation Steps
3. Database Setup
4. Admin Credentials Configuration
5. Running the Application
6. Testing the Application
7. Understanding the Code
8. Troubleshooting

---

## 1. Prerequisites

Before starting, make sure you have:
- **Python 3.8+** installed
- **MySQL Server** installed and running
- **Web browser** (Chrome, Firefox, or Edge)
- **Text editor** (VS Code, Sublime, or any editor)

---

## 2. Installation Steps

### Step 1: Install Python Dependencies

Open your terminal/command prompt and navigate to your project folder:

```bash
cd path/to/your/flask-crud-app
```

Install required Python packages:

```bash
pip install Flask flask-cors mysql-connector-python
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### Step 2: Verify MySQL Installation

Make sure MySQL is running on your computer. You can check by trying to connect:

```bash
mysql -u root -p
```

Enter your MySQL password when prompted. If it connects, MySQL is working!

---

## 3. Database Setup

### Option A: Automatic Setup (Recommended)
The application will automatically create the employee table when you first run it. Just make sure:

1. MySQL server is running
2. You have a database named `companydb`
3. Your MySQL credentials in `app.py` are correct

### Option B: Manual Setup

If you prefer to set up manually, follow these steps:

**Step 1: Log into MySQL**
```bash
mysql -u root -p
```

**Step 2: Create Database**
```sql
CREATE DATABASE IF NOT EXISTS companydb;
USE companydb;
```

**Step 3: Create Employee Table**
```sql
CREATE TABLE IF NOT EXISTS employee (
    Empid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
```

**Step 4: Verify Table**
```sql
SHOW TABLES;
DESCRIBE employee;
```

---

## 4. Admin Credentials Configuration

### Step 1: Set Your Admin Username and Password

Open `app.py` and find lines 16-17. Change the credentials to your desired values:

```python
# HARDCODED ADMIN CREDENTIALS - Change these to your desired username and password
ADMIN_USERNAME = "admin"       # Change this to your desired username
ADMIN_PASSWORD = "admin123"    # Change this to a strong password
```

**Example:**
```python
ADMIN_USERNAME = "superadmin"
ADMIN_PASSWORD = "MySecure@Password2024"
```

**IMPORTANT:** 
- These are the ONLY credentials that can access the system
- No registration is available - this is admin-only access
- Choose a strong password for security
- Remember these credentials as they're needed to login

---

## 5. Running the Application

### Step 1: Update Database Credentials

Open `app.py` and update the database connection with your credentials (lines 20-25):

```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",              # Your MySQL username
        password="8539980390@hk", # Your MySQL password
        database="companydb"      # Your database name
    )
```

### Step 2: Start the Flask Server

In your terminal, run:

```bash
python app.py
```

You should see output like:
```
🚀 Starting Flask Employee Management System...
📊 Backend running on http://127.0.0.1:5000
🔐 Authentication endpoints available
==================================================
✅ Database tables initialized successfully!
🔐 Admin Username: admin
🔐 Admin Password: admin123
 * Running on http://127.0.0.1:5000
```

**The terminal will show your admin credentials!**

**Important:** Keep this terminal window open! The server needs to keep running.

### Step 3: Open the Frontend

Open a web browser and navigate to:

**For login page:**
```
file:///path/to/your/flask-crud-app/login.html
```

Or simply double-click the `login.html` file to open it in your browser.

**Alternative:** Use a simple HTTP server (recommended)
```bash
# In a new terminal window
cd path/to/your/flask-crud-app
python -m http.server 5500
```

Then open: `http://localhost:5500/login.html`

---

## 6. Testing the Application

### Test 1: Admin Login

1. Open `login.html` in your browser
2. You'll see "Admin Access Only" badge
3. Enter your admin credentials:
   - Username: `admin` (or whatever you set)
   - Password: `admin123` (or whatever you set)
4. Click "Login"
5. You should be redirected to the dashboard

**Note:** If you try to login with wrong credentials, you'll get an "Invalid username or password" error.

### Test 2: Add Employee

1. On the dashboard, fill in the form:
   - Name: `John Doe`
   - Department: `IT`
   - Salary: `75000`
2. Click "Add Employee"
3. The employee should appear in the table below

### Test 3: Edit Employee

1. Find the employee in the table
2. Click "Edit" button
3. Change any field (e.g., salary to `80000`)
4. Click "Update"
5. The table should refresh with updated data

### Test 4: Delete Employee

1. Click "Delete" button next to an employee
2. Confirm the deletion
3. The employee should be removed from the table

### Test 5: Logout

1. Click "Logout" button in the top right
2. You should be redirected back to the login page
3. Try accessing `dashboard.html` directly - you should be redirected to login

---

## 7. Understanding the Code

### Backend (app.py)

#### Admin Credentials (IMPORTANT!)
```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
```
These are hardcoded in the backend. Only these credentials can access the system. Change them before deploying!

#### Database Connection
```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="8539980390@hk",
        database="companydb"
    )
```
This function creates a connection to your MySQL database.

#### Authentication Endpoint

**Login:** `/api/login` (POST)
- Takes username and password
- Compares against hardcoded admin credentials
- Creates a session if valid
- Returns user information or error

**Logout:** `/api/logout` (POST)
- Clears the user session
- Returns success message

**Check Auth:** `/api/check-auth` (GET)
- Checks if user is logged in
- Used to protect pages

#### CRUD Endpoints (All require authentication)

**Create:** `/api/employee` (POST)
- Adds new employee to database

**Read All:** `/api/employees` (GET)
- Retrieves all employees

**Read One:** `/api/employee/<id>` (GET)
- Retrieves specific employee

**Update:** `/api/employee/<id>` (PUT)
- Updates employee information

**Delete:** `/api/employee/<id>` (DELETE)
- Removes employee from database

#### Security Features

1. **Hardcoded Admin:** Only one set of credentials can access the system
   ```python
   if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
       # Grant access
   ```

2. **Session Management:** Uses Flask sessions to track logged-in admin
   ```python
   session['user_id'] = 1
   session['logged_in'] = True
   ```

3. **Authentication Decorator:** Protects routes
   ```python
   @login_required
   def get_employees():
       # Only accessible if logged in
   ```

4. **CORS:** Allows frontend to communicate with backend
   ```python
   CORS(app, supports_credentials=True)
   ```

### Frontend

#### login.html
- Single login form (no registration)
- Shows "Admin Access Only" badge
- Validates input
- Makes API calls to backend
- Shows success/error messages
- Redirects to dashboard on successful login

#### dashboard.html
- Protected page (redirects to login if not authenticated)
- Shows "Admin" in the navbar
- Form to add new employees
- Table displaying all employees
- Edit modal for updating employees
- Delete functionality with confirmation
- Logout button

---

## 8. Troubleshooting

### Problem: Can't login with credentials

**Solution:**
1. Check the terminal output - it shows your admin credentials
2. Make sure you're using the exact username and password from `app.py`
3. Credentials are case-sensitive
4. Check lines 16-17 in `app.py` for current credentials

### Problem: "Connection error" message

**Solution:**
1. Check if Flask server is running
2. Look at the terminal - should show `Running on http://127.0.0.1:5000`
3. If not, run `python app.py`

### Problem: "Authentication required" or redirects to login

**Solution:**
1. Make sure you're logged in with admin credentials
2. Check if cookies are enabled in your browser
3. Try using `python -m http.server 5500` instead of opening files directly

### Problem: Can't connect to database

**Solution:**
1. Check if MySQL is running:
   ```bash
   # Windows
   net start MySQL80
   
   # Mac
   mysql.server start
   
   # Linux
   sudo service mysql start
   ```

2. Verify credentials in `app.py`
3. Test connection manually:
   ```bash
   mysql -u root -p
   USE companydb;
   ```

### Problem: "Module not found" errors

**Solution:**
Install missing packages:
```bash
pip install Flask flask-cors mysql-connector-python
```

### Problem: CORS errors in browser console

**Solution:**
1. Make sure you're using the same origin for frontend and backend
2. Try using `python -m http.server 5500` to serve the HTML files
3. Check that CORS is properly configured in `app.py`

### Problem: Session not persisting

**Solution:**
1. Make sure `credentials: 'include'` is in all fetch requests
2. Check browser console for cookie errors
3. Try using HTTP server instead of file:// protocol

### Problem: Forgot admin password

**Solution:**
1. Stop the Flask server (Ctrl+C)
2. Open `app.py`
3. Change lines 16-17 to new credentials
4. Save and restart: `python app.py`

---

## 📝 Additional Notes

### Project Structure
```
flask-crud-app/
│
├── app.py              # Backend Flask application
├── login.html          # Admin login page (no registration)
├── dashboard.html      # Main application page
└── requirements.txt    # Python dependencies
```

### Admin Credentials
**Default credentials (CHANGE THESE!):**
- Username: `admin`
- Password: `admin123`

**To change:** Edit lines 16-17 in `app.py`

### Security Recommendations for Production

1. **Use environment variables for credentials:**
   ```python
   import os
   ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
   ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
   ```

2. **Use strong password:**
   - At least 12 characters
   - Mix of uppercase, lowercase, numbers, symbols
   - Example: `MyS3cur3@AdminP@ss2024!`

3. **Change the secret key:**
   ```python
   app.secret_key = 'your-very-secret-key-here'
   ```

4. **Enable HTTPS:**
   ```python
   app.config['SESSION_COOKIE_SECURE'] = True
   ```

5. **Add rate limiting to prevent brute force attacks**
6. **Use password hashing (for multiple admins in future)**
7. **Implement IP whitelisting for admin access**

### API Endpoints Summary

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/login` | POST | Admin login | No |
| `/api/logout` | POST | Logout | Yes |
| `/api/check-auth` | GET | Check if logged in | No |
| `/api/employee` | POST | Create employee | Yes |
| `/api/employees` | GET | Get all employees | Yes |
| `/api/employee/<id>` | GET | Get one employee | Yes |
| `/api/employee/<id>` | PUT | Update employee | Yes |
| `/api/employee/<id>` | DELETE | Delete employee | Yes |

---

## 🎉 Success!

If everything is working:
- ✅ You can login as admin
- ✅ You can add employees
- ✅ You can view the employee list
- ✅ You can edit employees
- ✅ You can delete employees
- ✅ You can logout
- ✅ No one else can create accounts or access the system

Congratulations! You now have a secure, admin-only Employee Management System with CRUD operations.

---

## 🔒 Security Notes

**This is an admin-only system:**
- No user registration available
- Only hardcoded admin credentials work
- Perfect for single-admin use cases
- Change default credentials immediately!
- Consider using environment variables for production

---

## 📚 Learning Resources

To learn more about Flask:
- Flask Official Documentation: https://flask.palletsprojects.com/
- Flask Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- Real Python Flask Tutorials: https://realpython.com/tutorials/flask/

---

## 🤝 Need Help?

If you encounter issues not covered here:
1. Check the browser console for JavaScript errors (F12)
2. Check the Flask terminal for backend errors and see your admin credentials
3. Verify your MySQL connection
4. Make sure all files are in the same directory
5. Ensure you're using the correct admin credentials from app.py

Happy coding! 🚀
