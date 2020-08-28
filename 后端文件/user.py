from config import db
from flask import request, session
from app import app
from database import cur

@app.route(' ', methods=['POST'])
def register():
    data = request.get_json() 
    username = data['username']
    password = data['password']
    cur.execute('select `username` from users where `username`=%s', (username,))
    result = cur.fetchall()
    if result:
        return {
            'errcode': 400,
            'errmsg': '该用户名已被注册'
        }, 400  
    cur.execute('insert into users (`username`, `password`) values (%s, %s)', (username, password))
    if cur.rowcount > 0:
        return {
        'errcode': 0,
        'errmsg': '注册成功'
    }, 200

    return {
    'errcode': 400,
    'errmsg': '出现错误~请重试'
    }, 400
@app.route('', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    cur.execute('select `id` from users where `username`=%s and `password`=%s', (username, password))
    result = cur.fetchone()
    
    if result:
        session['user_id'] = result[0]
        return {
            'errcode': 0,
            'errmsg': '登陆成功'
        }, 200
    return {
        'errcode': 401,
        'errmsg': '用户不存在或密码错误'
    }, 401