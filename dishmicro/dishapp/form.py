import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, TextAreaField, \
    SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, length

# form is from week 7 page 14 and week5  page9
#  the form that used to store user's information


#  imitate the official code to customize length check
from dishapp.models import User


def lenmax(max=-1):
    message = 'Must be shorter than %d characters long.' % (max)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l > max:
            raise ValidationError(message)

    return _length
# use the official code to customize length check
def lenmin(min=-1):
    message = 'Must longer than %d characters.' % (min)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min:
            raise ValidationError(message)

    return _length

# check whether the user is in the database
def checkuser():
    message = 'The username have been used'

    def _checkuser(form, field):
        name = field.data
        if User.query.filter(User.username == name).first():
            raise ValidationError(message)

    return _checkuser

# check whether the user is in the database
def checkemail():
    message = 'The username have been used'
    message2 = "please check email format"
    def _checkemail(form, field):
        email = field.data
        if User.query.filter(User.email == email).first():
            raise ValidationError(message)
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is None:
            raise ValidationError(message2)

    return _checkemail


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),lenmin(min=1)])
    password = PasswordField("Password", validators=[DataRequired(), lenmin(min=6)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Sign in")


# form is from week 7 page 30
#  the form that used to for signup
class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), checkuser(), lenmin(min=1)])
    email = EmailField("Email", validators=[DataRequired(),checkemail(), lenmin(min=1)])
    password = PasswordField("Password", validators=[DataRequired(), lenmin(min=6)])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), lenmin(min=6)])
    accept_rules = BooleanField('I accept the site rules', validators=[DataRequired()])
    submit = SubmitField("Sign in")




# the form that used for storing user's user detail
class ProfileForm(FlaskForm):
    dob = DateField('Date of Birth', validators=[DataRequired()])
    gender = RadioField('Gender', choices=['Male', 'Female'], validators=[DataRequired()])
    avatar = FileField('Your Avatar', default=None)
    country = SelectField(
        label='Your country',
        choices=(
            'China',
            'America',
            'Ireland',
            'India',
            'Japan',
            'Korea',
            'France',
            'Britain',
        )
        , validators=[DataRequired()]
    )
    submit = SubmitField('Update Profile')


# the form that used for storing dishes
class PostForm(FlaskForm):
    posttitle = StringField("Dishtitle", validators=[DataRequired(), lenmax(30)])
    postbody = TextAreaField('MicroPost', validators=[DataRequired(), lenmax(10000)])
    dish_pic = FileField('Your dish\'s picture', validators=[DataRequired()])
    submit = SubmitField('Add Post')


# the form that used for sift dishes
class SearchForm(FlaskForm):
    criteria = StringField("Search for dishes: ")
    search = SubmitField('Search')
    order = SelectField(
        label='Ordered by:',
        choices=(
            'From old to new',
            'From new to old',
            'First letter A-Z',
            'First letter Z-A',
            'Number of likes'
        )
    )
    filter = SubmitField('Confirm')
