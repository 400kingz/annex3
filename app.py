from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    business_name = request.form['businessName']
    email = request.form['email']
    message = request.form['message']

    # Create the email content
    email_content = f"Name: {name}\nBusiness Name: {business_name}\nEmail: {email}\nMessage: {message}"
    msg = MIMEText(email_content)
    msg['Subject'] = 'New Form Submission'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'flurpro@gmail.com'

    # Send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
