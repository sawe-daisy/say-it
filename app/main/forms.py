from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about yourself', validators=[Required()])
    submit= SubmitField('submit')
    

class AddPitch(FlaskForm):
    details = TextAreaField('Add your pitch', validators=[Required()])
    category = RadioField('Label', choices=[('val1', 'promotion'),('val2', 'interview'),('val3','product'),('val4','pickuplines')],validators=[Required()])
    submit = SubmitField('Submit')
