import os
import smtplib

from dotenv import load_dotenv
from datetime import datetime
from flask import Blueprint, redirect, url_for, render_template
from forms import ContactForm

routes = Blueprint("routes", __name__)

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

@routes.context_processor
def inject_current_year():
    """This method is setting the current year"""
    return {"current_year": datetime.now().year}

@routes.route("/")
def home():
    """This method create the route the Home page"""
    return render_template("index.html", page_title="Vlad Tomoiaga")

@routes.route("/about")
def about():
    """This method create the route the About page"""
    return render_template("about.html", page_title="About")

@routes.route("/contact", methods=["GET", "POST"])
def contact():
    """This method create the route to the Contact page. The user can complete the Form.
    If the Form is correct, the user can send the Form."""
    contact_form = ContactForm()

    if contact_form.delete.data:
        return redirect(url_for("routes.contact"))

    if contact_form.validate_on_submit():
        email = [contact_form.email.data, TO_EMAIL]
        send_email(contact_form.name.data, email, contact_form.subject.data, contact_form.message.data)
        return redirect(url_for("routes.contact"))

    return render_template("contact.html", form=contact_form, page_title="Contact")

def send_email(name, to_email, subject, message):
    """This method send an Email with the message from the form and in CC with your Email."""
    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to_email,
            msg=f"Subject:{subject} \nName: {name} \n{message}".encode("utf-8"))
