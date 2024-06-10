from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='soorya',
        database='student_management'
    )


# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


# Home route
@app.route('/')
def default():
    return redirect(url_for('login'))


# Home route
@app.route('/home')
@login_required
def home():
    return render_template('home.html')


# Delete admin route
@app.route('/delete_admin/<int:id>', methods=['POST'])
@login_required
def delete_admin(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM admins WHERE id = %s', (id,))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('view_admins'))


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM admins WHERE email = %s AND password = %s', (email, password))
        admin = cursor.fetchone()
        cursor.close()
        connection.close()

        if admin:
            session['logged_in'] = True
            session['admin_id'] = admin['id']
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')


# Logout route
@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


# Register student route
@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        department = request.form['department']
        section = request.form['section']
        email = request.form['email']
        phone = request.form['phone']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO students (name, student_id, department, section, email, phone) VALUES (%s, %s, %s, %s, %s, %s)',
            (name, student_id, department, section, email, phone))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('view_students'))

    return render_template('register.html')


# View students route
@app.route('/students')
@login_required
def view_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('students.html', students=students)


# Modify student route
@app.route('/modify/<int:id>', methods=['GET', 'POST'])
@login_required
def modify(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        department = request.form['department']
        section = request.form['section']
        email = request.form['email']
        phone = request.form['phone']

        cursor.execute(
            'UPDATE students SET name=%s, student_id=%s, department=%s, section=%s, email=%s, phone=%s WHERE id=%s',
            (name, student_id, department, section, email, phone, id))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('view_students'))

    cursor.execute('SELECT * FROM students WHERE id = %s', (id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('modify.html', student=student)


# Delete student route
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM students WHERE id = %s', (id,))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('view_students'))


# Add admin route
@app.route('/add_admin', methods=['GET', 'POST'])
@login_required
def add_admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO admins (email, password) VALUES (%s, %s)', (email, password))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('view_admins'))

    return render_template('add_admin.html')


# View admins route
@app.route('/admins')
@login_required
def view_admins():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM admins')
    admins = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('admins.html', admins=admins) 
if __name__ == '__main__':
    app.run(debug=True)
