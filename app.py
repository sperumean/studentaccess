from flask import Flask, jsonify, request, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database
students = {}

@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))

    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        # Add the student to our 'database'
        students[student_id] = student_name
        return redirect(url_for('manage_students'))

    # For GET requests, display the students
    return render_template('students.html', students=students)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Perform login validation here
        # If valid, set session and redirect to the index page
        session['logged_in'] = True
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        # Perform registration validation here
        # If valid, create a new user account and redirect to the login page
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005)
