#-*- coding:utf-8 -*-
from functools import wraps
from flask import session, redirect, abort, url_for, current_app
from flask_jwt import current_identity, _jwt_required, JWTError




def jwt_auth(realm=None,rights=[],admin=0):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                _jwt_required(realm or current_app.config['JWT_DEFAULT_REALM'])
                print(current_identity)
                if admin == 1 and current_identity.is_admin!=1:
                    abort(401)
            except Exception as e:
                raise JWTError('Bad Request', 'Invalid credentials')
            return fn(*args, **kwargs)
        return decorator
    return wrapper


