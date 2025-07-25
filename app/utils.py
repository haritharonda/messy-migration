# app/utils.py

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(hashed, user_password):
    return hashed == hashlib.sha256(user_password.encode()).hexdigest()

