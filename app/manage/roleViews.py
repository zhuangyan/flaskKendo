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

@manage.route('/roles/')
@MineAuthentic.auth(request,admin=1)
def roles_lists():

    return render_template('manage/roles_list.html',
                           title=u'角色'
                           )


@manage.route('/roles/add')
@MineAuthentic.auth(request,admin=1)
def roles_add():
    permissions_rows = []
    db = Db()
    select = {}
    where = {"status": 200, "sort": 1}
    order_by = {"order": 1}
    permissions = db.query("permissions", select=select, where=where, order_by=order_by)
    for u in permissions:
        name = u["name"]
        sort = u["sort"]
        permissions_rows.append({
            "_id": str(u["_id"]),
            "icon": u["icon"],
            "url": u["url"],
            "sort": sort,
            "name": name
        })
        permissions_sub = db.query("permissions", select=select, where={"status": 200, "parent_id": str(u["_id"])},
                                   order_by={"order": 1})
        for uu in permissions_sub:
            name = u" |-{} ".format(uu["name"])
            sort = uu["sort"]
            permissions_rows.append({
                "_id": str(uu["_id"]),
                "icon": uu["icon"],
                "url": uu["url"],
                "sort": sort,
                "name": name
            })
            permissions_sub2 = db.query("permissions", select=select,
                                        where={"status": 200, "parent_id": str(uu["_id"])},
                                        order_by={"order": 1})
            for uuu in permissions_sub2:
                name = u" | |- {}".format(uuu["name"])
                sort = uuu["sort"]
                permissions_rows.append({
                    "_id": str(uuu["_id"]),
                    "icon": uuu["icon"],
                    "url": uuu["url"],
                    "sort": sort,
                    "name": name
                })
    return render_template('manage/roles_add.html',
                           permissions_rows=permissions_rows,
                           title=u'角色'
                           )

@manage.route('/roles/<id>/edit')
@MineAuthentic.auth(request,admin=1)
def roles_edit(id):
    db = Db()
    where = {"_id": (id,)}

    role = db.query_one("roles",select={},where=where)

    permissions_rows = []
    select = {}
    where = {"status": 200,"sort":1}
    order_by = {"order": 1}
    permissions = db.query("permissions", select=select, where=where, order_by=order_by)
    for u in permissions:
        name = u["name"]
        sort = u["sort"]
        permissions_rows.append({
            "_id": str(u["_id"]),
            "icon": u["icon"],
            "url": u["url"],
            "sort": sort,
            "name": name
        })
        permissions_sub = db.query("permissions", select=select, where={"status": 200,"parent_id":str(u["_id"])}, order_by={"order":1})
        for uu in permissions_sub:
            name = u" |- {}".format(uu["name"])
            sort = uu["sort"]
            permissions_rows.append({
                "_id": str(uu["_id"]),
                "icon": uu["icon"],
                "url": uu["url"],
                "sort": sort,
                "name": name
            })
            permissions_sub2 = db.query("permissions", select=select, where={"status": 200, "parent_id": str(uu["_id"])},
                                       order_by={"order": 1})
            for uuu in permissions_sub2:
                name = u" | |- {}".format(uuu["name"])
                sort = uuu["sort"]
                permissions_rows.append({
                    "_id": str(uuu["_id"]),
                    "icon": uuu["icon"],
                    "url": uuu["url"],
                    "sort": sort,
                    "name": name
                })
    return render_template('manage/roles_edit.html',
                           role = role,
                           permissions_rows = permissions_rows,
                           title=u'角色'
                           )


