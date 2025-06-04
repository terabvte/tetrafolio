from flask import Flask, render_template, url_for, session, request
import smtplib
import random
import os
from dotenv import load_dotenv # Make sure this is in requirements.txt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file for local development
load_dotenv()

app = Flask(__name__, static_folder='assets') # Your static folder
# Vercel will use its own environment variables for deployed app
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))

# Access environment variables (EMAIL and PASSWORD should be set in Vercel UI)
# email = os.getenv("EMAIL") # Not strictly needed at global scope here
# password = os.getenv("PASSWORD") # Not strictly needed at global scope here


@app.route("/")
def home():
    dictionar = {1: "lorenzo.html", 2: "matei.html", 3: "matteo.html", 4: "marco.html"}
    last_num = session.get("last_num")
    num = random.randint(1, 4)

    while (num == last_num):
        num = random.randint(1, 4)

    session["last_num"] = num
    return render_template(dictionar[num])


@app.route("/matei", methods=['POST', 'GET'])
def matei():
    return render_template('matei.html')


@app.route("/lorenzo", methods=['POST', 'GET'])
def lorenzo():
    return render_template("lorenzo.html")


@app.route("/marco", methods=['POST', 'GET'])
def marco():
    return render_template("marco.html")


@app.route("/matteo", methods=['POST', 'GET'])
def matteo():
    return render_template("matteo.html")


@app.route("/contact-me-form", methods=['POST', 'GET'])
def contact_me():
    if request.method == "POST":
        try:
            name = request.form["name"]
            user_email = request.form["email"]
            message = request.form["userMessage"]

            # These will be fetched from Vercel's environment variables when deployed
            app_email = os.getenv("EMAIL")
            app_password = os.getenv("PASSWORD")

            if not app_email or not app_password:
                print("Email credentials missing. Ensure EMAIL and PASSWORD are set in Vercel environment variables.")
                return render_template('contact.html', msg_sent=False, error="Configuration error: Email credentials missing")

            msg = MIMEMultipart()
            msg['From'] = app_email
            msg['To'] = app_email # Sending to yourself
            msg['Subject'] = "Contact me form blog"

            body = f"Name: {name}\nEmail: {user_email}\nMessage: {message}"
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(app_email, app_password)
                server.send_message(msg)
            return render_template('contact.html', msg_sent=True)

        except Exception as e:
            print(f"Error sending email: {e}")
            return render_template('contact.html', msg_sent=False, error=str(e))

    return render_template('contact.html', msg_sent=False)


# This part is for local development only. Vercel will not run this.
if __name__ == "__main__":
    app.run(debug=True)
