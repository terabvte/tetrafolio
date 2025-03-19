from flask import Flask, render_template, url_for, session, request
import smtplib
import random
import os
from dotenv import load_dotenv

app = Flask(__name__, static_folder='assets')

#Acces enviroment variables
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


@app.route("/")
def home():

    dictionar = {1 : "lorenzo.html", 2 : "matei.html" , 3 : "matteo.html", 4 : "marco.html"}
    last_num = session.get("last_num")
    num = random.randint(1,4)

    while (num == last_num):
        num = random.randint(1,4)

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
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["userMessage"]

        my_email = email
        my_password = password

        with smtplib.SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(user=my_email, password=my_password)
            mail.sendmail(from_addr=my_email, to_addrs=my_email, msg=
                        f"Subject:Contact me form blog\n\nname: {name}\nemail: {email}\nmessage: {message}")

        return render_template('contact.html', msg_sent = True)
    return render_template('contact.html', msg_sent = False)


if __name__ == "__main__":
    app.run(debug=True)
