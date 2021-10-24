from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, TextAreaField, \
    SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

# form is from week 7 page 14 and week5  page9
#  the form that used to store user's information
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Sign in")
# form is from week 7 page 30
#  the form that used to for signup
class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password",validators=[DataRequired()])
    accept_rules = BooleanField('I accept the site rules', validators=[DataRequired()])
    submit = SubmitField("Sign in")
# the form that used for storing user's user detail
class ProfileForm(FlaskForm):
    dob = DateField('Date of Birth', validators=[DataRequired()])
    gender = RadioField('Gender', choices = ['Male','Female'], validators=[DataRequired()])
    avatar = FileField('Your Avatar',default=None)
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
    )
    submit = SubmitField('Update Profile')
# the form that used for storing dishes
class PostForm(FlaskForm):
    posttitle = StringField("Dishtitle", validators=[DataRequired()])
    postbody = TextAreaField('MicroPost', validators=[DataRequired()])
    submit = SubmitField('Add Post')
# the form that used for sift dishes
class SearchForm(FlaskForm):
    criteria = StringField("Search for dishes: ")
    search = SubmitField('Search')
    order = SelectField(
        label='Ordered by:',
        choices=(
            'Release time',
        'First letter A-Z',
        'First letter Z-A'
        )
    )
    filter = SubmitField('Confirm')

