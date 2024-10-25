
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL_ADD = 'http://api:8080/student/add'
API_URL_ALL = 'http://api:8080/student/all'

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        module_code = request.form['module_code']

        payload = {
            'student_id': student_id,
            'first_name': first_name,
            'last_name': last_name,
            'module_code': module_code
        }
        response = requests.post(API_URL_ADD, json=payload)
        if response.status_code == 200:
            return redirect(url_for('add_student'))
        else:
            return "An error occured. Check that you're not duplicating PK"
    return render_template('form.html')


@app.route('/all')
def get_all_students():
    response = requests.get(API_URL_ALL)
    if response.status_code == 200:
        students = response.json()
        return render_template('students.html', students=students)
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
