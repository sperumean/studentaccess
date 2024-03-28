from flask import Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)

# Mock database
students = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        # Add the student to our 'database'
        students[student_id] = student_name
        return redirect(url_for('manage_students'))

    # For GET requests, display the students
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005)
