#!/usr/bin/env python
from flask import Flask, render_template, request, abort, redirect, make_response
from werkzeug.security import check_password_hash
from Crypto.Cipher import AES
from Crypto.Util import Counter
import json
import os
import struct
import binascii


cookie = "15702c687ef9bd5751465626547845f5d93fa0cbd451797bf82133d0683e709fd1b70344c616b3e9ac0f64b1e8f735f4"
iv = unhexlify(cookie[:32])
print("This is IV " + str(iv))
cookie = unhexlify(cookie[32:])
cipher = AES.new(key, AES.MODE_CBC, iv)
cookie = cipher.decrypt(cookie)

while cookie[-1] != ord('1'):
    cookie = cookie[:-1]



