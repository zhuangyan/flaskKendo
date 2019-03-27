#!/usr/bin/env python
#-*- coding:utf-8 -*-
''''' 
Created on  
@author: zhuangyan 
'''
from bson import ObjectId
from flask import redirect, render_template, request

from com.minerequest import MineAuthentic
from com import reflections

from . import manage
import app.models


@manage.route('/permissions/')
@MineAuthentic.auth(request,admin=1)
def perms_lists():

    return render_template('manage/permissions_list.html',
                           title=u'权限'
                           )


@manage.route('/permissions/add')
@MineAuthentic.auth(request,admin=1)
def perms_add():

    parent_list = []
    db = Db()
    where = {"status": 200, "sort": 1}

    extras = reflections.reflect(app.models,reflections.module_extractor)

    models = []
    for q in extras:
        models.append(q[1])

    permissions = db.query('permissions', where=where, order_by={"order": 1})
    for u in permissions:
        subs = []
        where = {"status": 200, "sort": 2,"parent_id":str(u["_id"])}
        querys = db.query('permissions', where=where, order_by={"order": 1})
        for q in querys:
            subs.append({"_id":str(q["_id"]),"icon":q["icon"],"name":q["name"]})
        parent_list.append({
            "_id": str(u["_id"]),
            "icon": u["icon"],
            "url": u["url"],
            "sort": u["sort"],
            "subs": subs,
            "name": u["name"]
        })


    return render_template('manage/permissions_add.html',
                           parent_list = parent_list,
                           models = models,
                           title=u'权限'
                           )


@manage.route('/permissions/<id>/edit')
@MineAuthentic.auth(request,admin=1)
def perms_edit(id):
    extras = reflections.reflect(app.models, reflections.module_extractor)

    models = []
    for q in extras:
        models.append(q[1])
    db = Db()
    where = {"_id": (id,)}

    perm = db.query_one("permissions",select={},where=where)

    parent_name = ""
    if perm["parent_id"]:
        parent = db.query_one("permissions",select={},where={"_id":(perm["parent_id"],)})
        parent_name = parent["name"]

    return render_template('manage/permissions_edit.html',
                           perm = perm,
                           models = models,
                           parent_name=parent_name,
                           title=u'权限'
                           )


