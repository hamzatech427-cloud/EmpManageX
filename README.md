# 🏢 EmpManageX 

A secure web application for managing employee records with admin-only authentication, built with Flask (backend) and vanilla HTML/CSS/JavaScript (frontend).

[![GitHub](https://img.shields.io/badge/GitHub-EmpManageX-blue?logo=github)](https://github.com/kamalpanse18/EmpManageX)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)


## ✨ Features

### 🔐 Secure Admin Authentication
- **Hardcoded admin credentials** in backend (no registration)
- Single admin-only access
- Session management with Flask
- Protected routes
- Logout functionality
- No unauthorized user registration

### 👥 Employee Management (CRUD)
- **Create:** Add new employees with name, department, and salary
- **Read:** View all employees in a responsive table
- **Update:** Edit employee information via modal
- **Delete:** Remove employees with confirmation

### 🎨 Modern UI
- Beautiful gradient design
- Responsive layout (works on mobile, tablet, desktop)
- Real-time form validation
- Success/error message notifications
- Loading indicators
- Modal dialogs for editing
- "Admin Access Only" badge on login

### 🔒 Security Features
- Hardcoded credentials (single admin access)
- Session-based authentication
- Protected API endpoints
- SQL injection prevention (parameterized queries)
- CORS configuration for API security

## 📁 Project Structure

```
flask-crud-app/
│
├── app.py              # Flask backend with hardcoded admin credentials
├── login.html          # Admin login interface (no registration)
├── dashboard.html      # Employee management dashboard
├── requirements.txt    # Python package dependencies
├── SETUP_GUIDE.md     # Detailed setup instructions
├── QUICK_START.md     # Quick 5-minute setup guide
└── README.md          # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MySQL Server 8.0+
- Web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone or download this project**

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup MySQL database**
   ```sql
   CREATE DATABASE companydb;
   ```

4. **Configure admin credentials in `app.py` (lines 16-17)**
   ```python
   # HARDCODED ADMIN CREDENTIALS - Change these!
   ADMIN_USERNAME = "admin"       # Your desired username
   ADMIN_PASSWORD = "admin123"    # Your desired password
   ```

5. **Update database credentials in `app.py` (lines 20-25)**
   ```python
   def get_db_connection():
       return mysql.connector.connect(
           host="localhost",
           user="root",              # Your MySQL username
           password="your_password", # Your MySQL password
           database="companydb"
       )
   ```

6. **Run the Flask application**
   ```bash
   python app.py
   ```
   The terminal will display your admin credentials!

7. **Open the frontend**
   - Option A: Double-click `login.html`
   - Option B: Use a local server (recommended):
     ```bash
     python -m http.server 5500
     ```
     Then open: http://localhost:5500/login.html

## 📖 Usage

### Login as Admin
1. Open `login.html`
2. You'll see "Admin Access Only" badge
3. Enter your hardcoded admin credentials
4. Click "Login"
5. You'll be redirected to the dashboard

### Manage Employees
- **Add:** Fill the form at the top and click "Add Employee"
- **Edit:** Click "Edit" button next to an employee
- **Delete:** Click "Delete" button and confirm
- **Logout:** Click "Logout" in the top navigation

## 🔧 API Endpoints

### Authentication
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/login` | POST | Admin login only | No |
| `/api/logout` | POST | Logout admin | No |
| `/api/check-auth` | GET | Check authentication status | No |

### Employee CRUD (Protected)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/employee` | POST | Create new employee | Yes |
| `/api/employees` | GET | Get all employees | Yes |
| `/api/employee/<id>` | GET | Get employee by ID | Yes |
| `/api/employee/<id>` | PUT | Update employee | Yes |
| `/api/employee/<id>` | DELETE | Delete employee | Yes |

## 🗄️ Database Schema

### Employee Table
```sql
CREATE TABLE employee (
    Empid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
```

**Note:** No users table needed - authentication is hardcoded!

## 🛠️ Technologies Used

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **MySQL Connector** - Database connectivity

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradients and animations
- **JavaScript (ES6+)** - Interactivity and API calls
- **Fetch API** - HTTP requests

### Database
- **MySQL** - Relational database management

## 🔐 Security Features

This application implements several security measures:

1. **Hardcoded Admin Access**
   - Only one set of credentials hardcoded in backend
   - No user registration functionality
   - Perfect for single-admin systems

2. **SQL Injection Prevention**
   - Uses parameterized queries for all database operations
   - MySQL connector handles escaping automatically

3. **Session Security**
   - Secure session management with Flask
   - Configurable session timeout (24 hours default)

4. **Authentication**
   - Protected routes using `@login_required` decorator
   - Session validation on each request

5. **CORS Configuration**
   - Restricted origins for API access
   - Credentials support for cookie-based sessions

## ⚠️ Important Security Notes

### Default Credentials (CHANGE IMMEDIATELY!)
```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
```

### For Production Deployment

1. **Use environment variables**
   ```python
   import os
   ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
   ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
   ```

2. **Use strong password**
   - At least 12 characters
   - Mix of uppercase, lowercase, numbers, symbols
   - Example: `MyS3cur3@AdminP@ss2024!`

3. **Enable HTTPS**
   ```python
   app.config['SESSION_COOKIE_SECURE'] = True
   ```

4. **Update CORS origins**
   ```python
   CORS(app, origins=["https://yourdomain.com"])
   ```

5. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 app:app
   ```

6. **Add rate limiting** to prevent brute force attacks

7. **Consider IP whitelisting** for admin access

## 🐛 Troubleshooting

### Can't login
- Check terminal output for admin credentials
- Credentials are case-sensitive
- Check lines 16-17 in `app.py`

### Connection error
- Ensure Flask server is running (`python app.py`)
- Check if MySQL is running
- Verify database credentials

### Forgot password
- Stop server (Ctrl+C)
- Edit lines 16-17 in `app.py`
- Save and restart server

For more detailed troubleshooting, see `SETUP_GUIDE.md`.

## 📚 Documentation

- **SETUP_GUIDE.md** - Comprehensive setup instructions
- **QUICK_START.md** - Quick 5-minute setup
- **README.md** - This file

## 🎯 Perfect For

- Small businesses with single admin
- Internal company tools
- Personal projects
- Learning Flask and CRUD operations
- Systems requiring strict access control

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Created for learning purposes - Flask CRUD application with admin-only authentication.

## 🙏 Acknowledgments

- Flask documentation and community
- MySQL connector Python library

---

## 📞 Support

Need help? Check out:
1. `SETUP_GUIDE.md` for detailed instructions
2. `QUICK_START.md` for quick setup
3. Terminal output shows admin credentials when server starts
4. Browser console (F12) for frontend errors
5. Flask terminal for backend errors

---

**Made with ❤️ using Flask and MySQL**

**🔒 Admin-Only Access | No User Registration | Secure & Simple**
