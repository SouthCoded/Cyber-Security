from flask import Flask, render_template, request, abort, redirect, make_response
from werkzeug.security import check_password_hash
from Crypto.Cipher import AES
from Crypto.Util import Counter
import json
import os
import struct

from binascii import hexlify, unhexlify

app = Flask(__name__)

key = open("key", 'rb').read() # Key was removed
FLAG = open("flag.txt", 'r').read()

def to_bytes(s):
  return bytes([ord(c) for c in s])

def from_bytes(s):
  return ''.join(chr(c) for c in s)

def encrypt(cookie):
  cookie += b'1'
  while len(cookie) % 16:
    cookie += b'0'

  iv = os.urandom(16)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  encrypted_cookie = cipher.encrypt(cookie)

  return hexlify(iv) + hexlify(encrypted_cookie)

def decrypt(cookie):
  iv = unhexlify(cookie[:32])
  cookie = unhexlify(cookie[32:])
  cipher = AES.new(key, AES.MODE_CBC, iv)
  cookie = cipher.decrypt(cookie)

  while cookie[-1] != ord('1'):
    cookie = cookie[:-1]

  return cookie[:-1]

def do_login(user, password, admin):
  assert(len(password) < 50)

  auth = struct.pack('<I', len(user)) + struct.pack('<I', len(password)) + to_bytes(user) + to_bytes(password) + struct.pack('<I', admin)
  cookie = encrypt(auth)

  resp = make_response(redirect('/'))
  resp.set_cookie('auth', cookie)

  return resp

def load_cookie():
  cookie = {'user': '', 'admin': 0}

  auth = request.cookies.get('auth')
  if auth:
    try:
      auth = decrypt(auth)

      user_len = struct.unpack('<I', auth[:4])[0]
      password_len = struct.unpack('<I', auth[4:8])[0]

      cookie['user'] = from_bytes(auth[8:8+user_len])
      cookie['password'] = from_bytes(auth[8+user_len:8+user_len+password_len])
      cookie['admin'] = struct.unpack('<I', auth[8+user_len+password_len:8+user_len+password_len+4])[0]
    except:
      cookie = {'user': '', 'admin': 0}

  return cookie

@app.route('/')
def index():
  cookie = load_cookie()
  print(cookie)
  return render_template('index.html', user = cookie['user'], admin = cookie['admin'], cookie = cookie)

@app.route('/login', methods=['POST'])
def login():
  user =  request.form.get('user', '')
  password = request.form.get('password', '')

  if user == 'guest': # Accept any passwords for the guest account
    return do_login(user, password, 0)
  if user == 'admin' and check_password_hash('pbkdf2:sha1:1000$bTY1abU0$5503ae46ff1a45b14ff19d5a2ae08acf1d2aacde', password):
    return do_login(user, password, 1)
  return abort(403)

@app.route('/logout', methods=['GET'])
def logout():
  resp = make_response(redirect('/'))
  resp.set_cookie('auth', '', expires=0)
  return resp

@app.route('/admin', methods=['GET'])
def admin():
  cookie = load_cookie()
  if cookie['admin'] == 1:
    return render_template('admin.html', flag=FLAG) # Flag was removed

  return abort(403)

if __name__ == '__main__':
  app.run(debug = True, host="0.0.0.0", port=1337)
