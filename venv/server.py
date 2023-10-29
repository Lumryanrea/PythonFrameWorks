from flask import Flask,render_template, request

import csv

app = Flask(__name__, template_folder='templates')

@app.route('/')
def html_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def welcome(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
    return render_template('thanks.html')


def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db_file:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer.writerow([name, email, subject, message])
        


