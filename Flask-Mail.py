from flask import Flask, Markup, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config.update(
    DEBUG = True,
    #EMAIL SETTINGS
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'nansquared@gmail.com',
    MAIL_PASSWORD = '*****'
    )

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mail", methods = ['GET', 'POST'])
def mail():
    if request.method == 'POST':
        username = request.form['email_address']
        userInput = request.form['mail_message']

        msg = Message("Hello",
                      sender = "nansquared@gmail.com",
                      recipients = ["nannan.yao@nyu.edu"])
        msg.body = userInput
        mail.send(msg)
        return Markup("<h1>Flask Mail Example</h1> <br><br><h2>Sent Mail</h2>")
    elif request.method == 'GET':
        return render_template("mail-example.html")


"""

    msg = Message("Hello",
                  sender = "nansquared@gmail.com",
                  recipients = ["nannan.yao@nyu.edu"])
    msg.body = "This is a test email sent out using Flask"
    mail.send(msg)
    return Markup("<h1>Flask Mail Example</h1> <br><br><h2>Sent Mail</h2>")


"""

if __name__ == "__main__":
    app.run()
