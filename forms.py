from flask.ext.wtf import Form
from wtforms import BooleanField, SelectField, HiddenField, TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

class NewStoryForm(Form):
	title = TextField(u'Title', validators=[DataRequired()])
	description = TextAreaField(u'Description (optional)')
	anonymous = BooleanField(u'Anonymous?', default=True)

class WriteForm(Form):
	prev_page = SelectField(u'Previous Page', coerce=int)
	title = TextField(u'Page Title', validators=[DataRequired()])
	text = TextAreaField(None, validators=[DataRequired()])

class LoginForm(Form):
	username = TextField(u'Username', validators=[DataRequired()])
	password = PasswordField(u'Password', validators=[DataRequired()])

class RegisterForm(Form):
	name = TextField(u'Name', validators=[DataRequired(), Length(max=25)])
	username = TextField(u'Username', validators=[DataRequired(), Length(max=16)])
	password = PasswordField(u'Password', validators=[DataRequired(), EqualTo('password_confirm', message="Passwords don't match")])
	password_confirm = PasswordField(u'Password, again', validators=[DataRequired()])

class UserEditForm(Form):
	name = TextField(u'Name', validators=[DataRequired(), Length(max=25)])
	bio = TextAreaField(u'Bio')

class UserEditLoginForm(Form):
	username = TextField(u'Username', validators=[DataRequired(), Length(max=16)])
	password = PasswordField(u'New Password', validators=[DataRequired(), EqualTo('password_confirm', message="Passwords don't match")])
	password_confirm = PasswordField(u'New Password, again', validators=[DataRequired()])
	old_password = PasswordField(u'Old Password', validators=[DataRequired()])
