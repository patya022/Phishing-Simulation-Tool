# Phishing-Simulation-Tool
This project demonstrates a Phishing Simulation Tool designed to educate users about identifying phishing attacks. The tool simulates phishing emails, creates fake login pages, and logs user interactions to help improve cybersecurity awareness.
Key Features:
Phishing Email Simulation: Sends fake phishing emails to users.
Fake Login Pages: Mimics legitimate login pages to test user responses.
Feedback System: Provides immediate feedback to users based on their actions (clicking links, entering credentials).
User Logging: Tracks which users interact with phishing attempts to evaluate the effectiveness of the awareness training.
Technologies Used:
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Database: SQLite
Email Automation: smtplib, Mailgun API (for sending phishing emails)
Installation and Usage:
Clone the repository to your local machine:
bash-
git clone https://github.com/yourusername/phishing-simulation-tool.git

Navigate to the project folder:
bash-
cd phishing-simulation-tool

Install dependencies:
bash-
pip install -r requirements.txt

Run the Flask application:
bash-
python app.py

Access the tool at http://127.0.0.1:5000/ in your web browser.

Contributions:
Feel free to fork the repository and make improvements. Contributions, bug fixes, or suggestions are welcome!

License:
This project is licensed under the MIT License - see the LICENSE file for details.
