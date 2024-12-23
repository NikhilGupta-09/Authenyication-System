import qrcode
import secrets
import time
from tkinter import Tk, Label
from PIL import Image, ImageTk
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variables to store session data and QR image
session_token = None
qr_img = None
img_displayed = False

def generate_login_qr():
    global session_token, qr_img
    # Generate a unique, random token for the session
    session_token = secrets.token_urlsafe(16)
    qr_data = f"https://github.com/NikhilGupta-09"  # URL for token validation

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill="black", back_color="white")
    return qr_img

def show_qr_in_window():
    global img_displayed
    root = Tk()
    root.title("QR Code Login")

    # Generate the QR code
    qr_img = generate_login_qr()

    # Convert the image for Tkinter compatibility
    qr_img_tk = ImageTk.PhotoImage(qr_img)

    # Display the QR code in the Tkinter window
    label = Label(root, image=qr_img_tk)
    label.image = qr_img_tk  # Keep a reference to avoid garbage collection
    label.pack()

    # Set a timer to close the window after 60 seconds or once validated
    root.after(60000, root.quit)  # Close after 60 seconds if not scanned

    # Display the window
    img_displayed = True
    root.mainloop()
    img_displayed = False

def close_qr():
    global img_displayed
    img_displayed = False  # This will close the Tkinter window

@app.route('/validate', methods=['GET'])
def validate_qr():
    token = request.args.get('token')
    if token == session_token:
        close_qr()
        return jsonify({"status": "success", "message": "QR code scanned successfully!"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid token."}), 400

def start_server():
    app.run(port=5000)

if __name__ == "__main__":
    # Start the server in a separate thread
    threading.Thread(target=start_server, daemon=True).start()

    # Show the QR code in a Tkinter window
    show_qr_in_window()
