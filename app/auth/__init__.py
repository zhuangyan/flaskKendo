#-*- coding:utf-8 -*-
from bson.objectid import ObjectId
from flask import Blueprint, jsonify

# Create a Flask Blueprint which will define views and errors
import settings
from com.utils import encrypt_password
from app import mongo

auth = Blueprint(
    'auth',  # blueprint name
    __name__  # module where blueprint is located
)

# This Blueprint is defined as a Package named 'auth'.  The modules imported
# below are part of the Blueprint.  The views module must be imported after
# the Blueprint object is instantiated because it relies on the Blueprint
# object to define routes
from . import views
import datetime
from com import utils


class User(object):
    def __init__(self, id, username, gender=0,is_admin=0,rights=[],avatar=""):
        self.id = id
        self.username = username
        self.gender = gender
        self.is_admin = is_admin
        self.avatar = avatar
        self.rights = rights

    def __str__(self):
        return "User(id='%s')" % self.id

class Auth():
    def authenticate(self, username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param password:
        :return: json
        """
        db = mongo.db
        user = db.user.find_one({"username": username})
        if (user is None):
            return None
        else:
            if encrypt_password(password)==user["password"]:
                return User(str(user["_id"]), user["username"]
                            ,is_admin=user["is_admin"]
                            ,avatar=user.get("avatar",""))
    def identity(self, payload):
        """
        用户鉴权
        :return: list
        """
        user_id = payload['identity']
        db = mongo.db
        user = db.user.find_one({"_id": ObjectId(user_id)})
        if user:
            return User(str(user["_id"]), user["username"]
                        , is_admin=user["is_admin"]
                        , avatar=user.get("avatar", ""))

