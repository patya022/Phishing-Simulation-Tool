import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database setup
def setup_database():
    conn = sqlite3.connect('phishing_simulation.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT,
                        clicked_link BOOLEAN,
                        entered_credentials BOOLEAN)''')
    conn.commit()
    conn.close()

# Email simulation function
def send_phishing_email(target_email, fake_login_url):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    subject = "Important Account Update"
    body = f"Please verify your account details by clicking on this link: {fake_login_url}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        server.quit()
        print(f"Phishing email sent to {target_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Fake login page
@app.route('/login', methods=['GET', 'POST'])
def fake_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        log_response(email, clicked_link=True, entered_credentials=True)
        return render_template('feedback.html', message="This was a phishing simulation. Learn to identify phishing emails!")
    return render_template('login.html')

# Feedback route
@app.route('/feedback', methods=['GET'])
def feedback():
    return render_template('feedback.html', message="This was a phishing simulation. Learn to identify phishing emails!")

# Simulation route
@app.route('/simulate', methods=['POST'])
def simulate():
    target_email = request.form['email']
    fake_login_url = url_for('fake_login', _external=True)
    send_phishing_email(target_email, fake_login_url)
    return render_template('simulate.html', message="Phishing email sent successfully!")

# Logging responses
def log_response(email, clicked_link=False, entered_credentials=False):
    conn = sqlite3.connect('phishing_simulation.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO results (email, clicked_link, entered_credentials) 
                      VALUES (?, ?, ?)''', (email, clicked_link, entered_credentials))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
