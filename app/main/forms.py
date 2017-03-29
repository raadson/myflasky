#coding=utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User

class NameForm(Form):
    name = StringField('what is your name?',validators=[DataRequired()])
    submit = SubmitField('submit')

class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0,64)])
    location = StringField('Location', validators=[Length(0,64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

class PostForm(Form):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class Calc24Form(Form):
    number1 = IntegerField(u'输入一个整数(1~10)', validators=[
        DataRequired(u'请输入一个有效的整数！'),
        NumberRange(0, 10, u'请输入0~10以内的整数！')])
    number2 = IntegerField(u'输入一个整数(1~10)', validators=[
        DataRequired(u'请输入一个有效的整数！'),
        NumberRange(0, 10, u'请输入0~10以内的整数！')])
    number3 = IntegerField(u'输入一个整数(1~10)', validators=[
        DataRequired(u'请输入一个有效的整数！'),
        NumberRange(0, 10, u'请输入0~10以内的整数！')])
    number4 = IntegerField(u'输入一个整数(1~10)', validators=[
        DataRequired(u'请输入一个有效的整数！'),
        NumberRange(0, 10, u'请输入0~10以内的整数！')])
    submit = SubmitField(u'计算')

class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username', validators=[DataRequired(),Length(1,64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                    'Usernames must have only letters, '
                                                    'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0,64)])
    location = StringField('Location', validators=[Length(0.64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    def __init__(self,user,*args,**kwargs):
        super(EditProfileAdminForm,self).__init__(*args,**kwargs)
        self.role.choices = [(role.id,role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user
    def validate_email(self,field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self,field):
        if field.data !=self.user.username and \
                User.query.filter_by(usernmae=field.data).first():
            raise ValidationError('Username already registered.')