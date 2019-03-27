# coding=utf-8
import datetime, time
import re as regex
import json
import os
import hashlib






def encrypt_password(password):
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

