# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:11:49 2021

@author: Sanjay G R
"""

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')
