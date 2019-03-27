#!/usr/bin/env python
#-*- coding:utf-8 -*-
''''' 
Created on  
@author: zhuangyan 
'''
from flask import Blueprint

# Create a Flask Blueprint which will define views and errors
manage = Blueprint(
    'manage',  # blueprint name
    __name__  # module where blueprint is located
)

from . import userViews
from . import roleViews
from . import permissionViews
