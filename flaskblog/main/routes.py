# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:11:49 2021

@author: Sanjay G R
"""

from flask import render_template, request
from flaskblog.models import Post


from flask import Blueprint

main = Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page,per_page=5)
    return render_template('home.html',title='Ma sguy',posts=posts)

@main.route('/about')
def about():
    return render_template('about.html',title='Ma sguy')