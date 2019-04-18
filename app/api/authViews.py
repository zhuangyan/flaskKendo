#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''''
Created on
@author: zhuangyan
'''
import datetime
import json
import os
import uuid

from bson import ObjectId
from flask import Flask, Response, jsonify, request, session
from flask_jwt import jwt_required, current_identity
from flask_uploads import UploadSet, extension
from PIL import Image


from com.utils import encrypt_password
from app import mongo

from . import api

@api.route('/auth/password/',methods=['POST'])
@jwt_required()
def password():
    userid = current_identity.id
    pdata = request.json
    oldpassword = pdata['oldpassword'].strip()
    newpassword = pdata['newpassword'].strip()
    # print(records)
    user = mongo.db.user.find_one({"_id":ObjectId(userid)})
    if user and encrypt_password(oldpassword)==user["password"]:
        result = {
            "result": "y",
            "msg": ""
        }
    else:
        result = {
            "result": "n",
            "msg": "旧密码错误"
        }

    return Response(json.dumps(result, indent=4), mimetype='application/json')