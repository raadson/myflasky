#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class NameForm(FlaskForm):
    name = StringField('what is your name?',validators=[DataRequired()])
    submit = SubmitField('submit')

class Calc24Form(FlaskForm):
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