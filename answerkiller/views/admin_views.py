# -*- coding: utf-8 -*-
from flask import Blueprint, request, g, render_template, jsonify
from answerkiller import login_manager


admin_bp = Blueprint('Admin', __name__, subdomain='admin')


@admin_bp.route('/orders', methods=['GET'])
@admin_bp.route('/orders/<order_id>', methods=['GET'])
def orders(order_id=None):
    if not order_id:
        resp = {'count': 4, 'items':[{'name':'Computer Science', 'status':'Completed',
        'id':'OD32000123', 'created_at':'2014-03-08 14:00:20',
        'deadline':'2014-03-12 14:00:20',
        'last_update':'2014-03-09 14:00:20'},
        {'name':'Computer Science', 'status':'Processing',
        'id':'OD32000114', 'created_at':'2014-03-08 14:00:20',
        'deadline':'2014-03-12 14:00:20',
        'last_update':'2014-03-09 14:00:20'},
        {'name':'Computer Science', 'status':'Created',
        'id':'OD32000135', 'created_at':'2014-03-08 14:00:20',
        'deadline':'2014-03-12 14:00:20',
        'last_update':'2014-03-09 14:00:20'},
        {'name':'Computer Science', 'status':'Paid',
        'id':'OD32000125', 'created_at':'2014-03-08 14:00:20',
        'deadline':'2014-03-12 14:00:20',
        'last_update':'2014-03-09 14:00:20'}
        ]}
        return jsonify(resp)
    return order_id


@admin_bp.route('/orders', methods=['POST'])
def create_order():
    request_body = {'name':'Geometrics', 'course':'Mathematics',
    'deadline':'2014-03-15 14:00:20','customer_id':'wangerqiang',
    'cs_id':'zhangsan','prepaid':80, 'description':'Be fast, blabla'
    }
    resp = {'id': 'OD32000115', 'status': 'Success'}
    return jsonify(resp)


@admin_bp.route('/courses', methods=['GET'])
@admin_bp.route('/courses/<id>', methods=['GET'])
def courses(id=None):
    pass


@admin_bp.route('/courses', methods=['POST'])
def create_courses():
    request_body = {'id': '2', 'name':'Psychology', 'course':'Mathematics',
    'min_fee':80, 'description':'asodi sdjka jlsd  jxkuut ms djksd'
    }
    resp = {'id': '1', 'status': 'Success'}
    return jsonify(resp)


@admin_bp.route('/courses/<id>', methods=['POST'])
def edit_course(id):
    request_body = {'id': '2','name':'Psychology', 'course':'Mathematics',
    'min_fee':80, 'description':'asodi sdjka jlsd  jxkuut ms djksd'
    }
    resp = {'id': '1', 'status': 'Success'}
    return jsonify(resp)


@admin_bp.route('/courses/<id>/textbooks', methods=['POST'])
def add_books(course_name):
    pass


@admin_bp.route('/users', methods=['GET'])
def users():
    resp = {'count': 4, 'items':[{'username':'dajibaliang', 'type':'cs', 'permission': 2,
    'gender': u'男生', 'email':'dajibaliang@163.com'},
    {'username':'zhangbiaozi', 'type':'cs', 'permission': 3, 'gender': u'男生',
    'email':'zhangbiaozi@163.com'},
    {'username':'wangerbiao', 'type':'customer', 'permission': 0, 'gender': u'男生',
    'email':'wangerbiao@163.com'},
    {'username':'ganniniang', 'type':'tutor', 'permission': 1, 'gender': u'男生',
    'email':'ganniniang@163.com'}]}

    return jsonify(resp)


@admin_bp.route('/textbooks/<id>/answers', methods=['POST'])
def add_answer(id):
    pass