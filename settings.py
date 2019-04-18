#!/usr/bin/env python
#-*- coding:utf-8 -*-
''''' 
Created on  
@author: zhuangyan 
'''
from datetime import timedelta


class Config(object):
    DEBUG               = True
    SECRET_KEY          = 'a[U\\^U;N_OGX5WG+9F\:ba[U\\^yA|Nx|xf6"^'
    JWT_AUTH_URL_RULE = "/_api/auth/"
    MONGO_URI = "mongodb://127.0.0.1:27017/kendo"



