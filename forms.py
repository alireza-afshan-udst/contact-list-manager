from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TelField
from wtforms.validators import InputRequired, Email, Length, Regexp


class ContactForm(FlaskForm):
    name = StringField('Name',
                        validators=[
                            InputRequired(message="Name required."),
                            Length(min=2, max=50, message="Must be between 2 and 50 letters long."),
                            ])
    phone = TelField('Phone',
                        validators=[
                            InputRequired(message="Phone required."),
                            Regexp("^\d\d\d\d\s\d\d\d\d$", message="Must look like '1234 5678'")
                            
                            ])
    email = StringField('Email',
                        validators=[
                            InputRequired(message="Email required."),
                            Email(message="Must be a valid email.")
                            ])
    type = SelectField('Type', 
                        choices=[
                            ('Personal', 'Personal'), 
                            ('Work', 'Work'), 
                            ('Other', 'Other')
                            ])
    submit = SubmitField('Submit') 