from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

def run_face_auth():
    subprocess.run(["python", "face_auth.py"])

def run_otp_auth():
    subprocess.run(["python", "otp_auth.py"])

def run_qr_auth():
    subprocess.run(["python", "qr_auth.py"])

@app.route('/')
def home():
    return render_template('Authentication_system.html')

@app.route('/run-auth', methods=['POST'])
def run_auth():
    auth_type = request.form['auth_type']
    if auth_type == 'otp':
        run_otp_auth()
    elif auth_type == 'face':
        run_face_auth()
    elif auth_type == 'qr':
        run_qr_auth()
    return "Authentication process started!", 200

if __name__ == "__main__":
    app.run(debug=True)
