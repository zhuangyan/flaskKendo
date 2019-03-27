#!/usr/bin/env python
#-*- coding:utf-8 -*-
''''' 
Created on  
@author: zhuangyan 
'''
from mongoengine import Document
from mongoengine import IntField, FloatField, DateTimeField, StringField, ReferenceField, ListField


class User(Document):
    name = StringField(unique=True, required=True)
    password = StringField()
    email = StringField()
    phone = StringField()
    account = StringField()
    gender = IntField()
    status = IntField()
