#coding=utf-8
from flask import render_template, redirect, url_for, flash, abort,request,current_app
from flask_login import login_required, current_user
from . import main
from .forms import NameForm, Calc24Form,PostForm, EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import User, Post, Role, Permission
import itertools as it
from .calc24 import Calc24
from ..decorators import admin_required

#处理博客文章
@main.route('/',methods=['GET','POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
        form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    #博客分页
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page,per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    posts = pagination.items  #当前页面中的记录 也就是20条
    return render_template('index.html', form=form, posts=posts,pagination=pagination)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()#某个用户所有博客
    return render_template('user.html',user=user, posts=posts)

#用户编辑更改信息
@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

#管理员编辑用户信息
@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has beenupdated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)

#文章的固定链接
@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])

@main.route('/semantic',methods=['GET','POST'])
def semantic():
    return render_template('semanticweb.html')

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
