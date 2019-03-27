#!/usr/bin/env python
#-*- coding:utf-8 -*-
''''' 
Created on  
@author: zhuangyan 
'''
from bson import ObjectId
from flask import render_template, redirect, request

from com.minerequest import MineAuthentic
from . import manage


@manage.route('/users/')
@MineAuthentic.auth(request,admin=1)
def users_lists():

    return render_template('manage/users_list.html', title=u'用户')


@manage.route('/users/add')
@MineAuthentic.auth(request,admin=1)
def users_add():

    return render_template('manage/users_add.html', title=u'用户')

@manage.route('/users/<id>')
@MineAuthentic.auth(request, admin=1)
def users_edit(id):
    db = Db()

    user = db.query_one('users', where={"_id": (id,), "status": 200})

    return render_template('manage/users_edit.html', user=user, title=u'用户')

@manage.route('/users/<id>/role')
@MineAuthentic.auth(request, admin=1)
def users_role(id):
    db = Db()

    user = db.query_one('users', where={"_id": (id,)})
    roles_query = db.query('roles', where={"status": 200})
    roles = []
    for r in roles_query:
        roles.append({
            "id":str(r["_id"]),
            "name":r["name"]
        })

    return render_template('manage/users_role.html', user=user, roles=roles, title=u'用户')


@manage.route('/users/profile')
@MineAuthentic.auth(request,admin=1)
def users_profile():
    db = Db()

    user = db.query_one('users', where={"_id": (id,), "status": 200})

    return render_template('manage/users_profile.html', user=user, title=u'用户')
