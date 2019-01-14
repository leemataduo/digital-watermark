# -*- coding: UTF-8 -*-
from flask import render_template, redirect, url_for, request

from blueprints import home

@home.route('/')
def index():
   name=None
   #message='please login or register before use this function'    
   return render_template("index.html",name=name)

