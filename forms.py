from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, Email


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[Length(min=2, message="Field must be at least 2 characters long.")])
    email = StringField(label="Email", validators=[Email()])
    subject = StringField(label="Subject",
                          validators=[Length(min=2, message="Field must be at least 2 characters long.")])
    message = TextAreaField(label="Message",
                            validators=[Length(max=2000, message="Field must be maximum 2000 characters long.")])
    submit = SubmitField(label="Send Message")
    delete = SubmitField(label="Clear Form")