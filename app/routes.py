from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_mail import Message
from app import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/discover")
def discover():
    return render_template("discover.html")


@app.route("/nursery")
def nursery():
    return render_template("nursery.html")


@app.route("/bedtime")
def bedtime():
    return render_template("bedtime.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/contact", methods=['GET'])
def contact_form():
    return render_template("contact.html")

# Маршрут для обработки формы (метод POST)
@app.route("/contact", methods=['POST'])
def contact_post():
    from . import mail  # Подключение модуля почты

    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message_body = request.form['message']

    msg = Message(
        subject=f"New message from {name}: {subject}",
        sender=email,
        recipients=['your-receiving-email@gmail.com']
    )
    msg.body = message_body

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send message: {str(e)}", "danger")

    return redirect(url_for('main.contact_form.html'))
