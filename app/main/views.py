#coding=utf-8
from datetime import datetime
from flask import render_template, session,redirect, url_for, flash
from . import main
from .forms import NameForm, Calc24Form
from .. import db
from ..models import User
import itertools as it
from .calc24 import Calc24

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    # user = {'nickname':'adson'}
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template("index.html",
                           form=form,name=session.get('name'),
                           known=session.get('known',False),
                           current_time=datetime.utcnow()
                           )

@main.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@main.route('/calc24',methods=['GET','POST'])
def calc24():
    form = Calc24Form()
    if form.validate_on_submit():
        a = form.number1.data
        b = form.number2.data
        c = form.number3.data
        d = form.number4.data
        list_sum = []
        for i in set(it.permutations([a,b,c,d])):
            Calc24(i, list_sum)
        for e in list_sum:
            flash(u'很厉害，计算结果是：' + e, 'success')#没显示处理?
            # return redirect(url_for('main.calc24'))
    return render_template('calc24.html', form=form)
