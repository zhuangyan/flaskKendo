#-*- coding:utf-8 -*-
import json

from bson import ObjectId
from flask import render_template, redirect, request, url_for, flash, session, g, Response

from . import auth
from com.utils import encrypt_password
from app import mongo


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pdata = request.json
        username = pdata['username']
        password = pdata['password']
        db = mongo.db
        where = {"username": username}
        try:
            user = db.user.find_one(where)
            if user and encrypt_password(password)==user["password"]:

                session["user_name"] = user["username"]
                session["user_id"] = str(user["_id"])
                if "avatar" in user:
                    session["user_avatar"] = user["avatar"]
                else:
                    session["user_avatar"] = "/static/images/head0.jpeg"

                is_admin = user["is_admin"] if "is_admin" in user else 0
                session["user_isadmin"] = is_admin
                # 用户权限
                user_rights = []

                # 用户菜单
                user_menus = []

                session["user_menus"] = user_menus
                session["user_rights"] = user_rights


            else:
                result = {
                    "result": "n",
                    "msg": "用户名或密码错误！"
                }
                return Response(json.dumps(result, indent=4), mimetype='application/json')

        except Exception as e:
            print(e)
            user = None

        if user:
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash(u'用户不存在', 'error')
    return render_template('auth/login.html')

