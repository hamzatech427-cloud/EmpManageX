# ⚡ Quick Start Guide

## 3-Step Setup

### 1. Install Dependencies
```bash
pip install Flask flask-cors mysql-connector-python
```

### 2. Setup MySQL Database
```bash
mysql -u root -p
```
```sql
CREATE DATABASE companydb;
EXIT;
```

### 3. Configure Admin Credentials (Optional)
Edit `app.py` lines 17-18 to change default credentials:
```python
ADMIN_USERNAME = "admin"      # Change this
ADMIN_PASSWORD = "admin123"   # Change this
```

### 4. Update Database Connection
Edit `app.py` lines 21-27 with your MySQL credentials:
```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",              # Your MySQL username
        password="8539980390@hk", # Your MySQL password  
        database="companydb"
    )
```

### 5. Run the Application
```bash
python app.py
```

### 6. Open in Browser
Go to: **http://127.0.0.1:5000**

That's it! Login with:
- Username: `admin`
- Password: `admin123`

---

## What You'll See

**Terminal Output:**
```
🚀 Starting Flask Employee Management System...
📊 Backend running on http://127.0.0.1:5000
🌐 Open http://127.0.0.1:5000 in your browser
🔐 Authentication endpoints available
==================================================
✅ Database tables initialized successfully!
🔐 Admin Username: admin
🔐 Admin Password: admin123
```

**In Browser:**
1. Visit http://127.0.0.1:5000
2. You'll see the login page
3. Enter admin credentials
4. Get redirected to dashboard automatically
5. Manage employees!

---

## Troubleshooting

**MySQL Connection Error?**
```bash
# Make sure MySQL is running
mysql -u root -p

# Check if database exists
SHOW DATABASES;
```

**Module Not Found?**
```bash
pip install Flask flask-cors mysql-connector-python
```

**Forgot Password?**
- Stop server (Ctrl+C)
- Edit lines 17-18 in app.py
- Restart: `python app.py`

---

## Need Detailed Instructions?
See `SETUP_GUIDE.md` for complete step-by-step guide.
