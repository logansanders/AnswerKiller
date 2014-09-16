# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, jsonify, \
    redirect, url_for, helpers
from flask.ext.login import login_required
from answerkiller.models import course
from answerkiller.utils import fileoperation
from answerkiller import db


admin_bp = Blueprint('Admin', __name__,
                     template_folder='../templates/admin',
                     static_folder='../templates/admin',
                     static_url_path='/')


@admin_bp.route('/orders', methods=['GET'])
@admin_bp.route('/orders/<order_id>', methods=['GET'])
def orders(order_id=None):
    if not order_id:
        resp = {'count': 4, 'items': [{'name': 'Computer Science',
                                       'status': 'Completed',
                                       'id': 'OD32000123',
                                       'created_at': '2014-03-08 14:00:20',
                                       'deadline': '2014-03-12 14:00:20',
                                       'last_update': '2014-03-09 14:00:20'},
                                      {'name': 'Computer Science',
                                      'status': 'Processing',
                                       'id': 'OD32000114',
                                       'created_at': '2014-03-08 14:00:20',
                                       'deadline': '2014-03-12 14:00:20',
                                       'last_update': '2014-03-09 14:00:20'},
                                      {'name': 'Computer Science',
                                      'status': 'Created',
                                       'id': 'OD32000135',
                                       'created_at': '2014-03-08 14:00:20',
                                       'deadline': '2014-03-12 14:00:20',
                                       'last_update': '2014-03-09 14:00:20'},
                                      {'name': 'Computer Science',
                                      'status': 'Paid',
                                       'id': 'OD32000125',
                                       'created_at': '2014-03-08 14:00:20',
                                       'deadline': '2014-03-12 14:00:20',
                                       'last_update': '2014-03-09 14:00:20'}
                                      ]}
        return jsonify(resp)
    return order_id


@admin_bp.route('/orders', methods=['POST'])
def create_order():

    request_body = {'name': 'Geometrics', 'course': 'Mathematics',
                    'deadline': '2014-03-15 14:00:20',
                    'customer_id': 'wangerqiang',
                    'cs_id': 'zhangsan', 'prepaid': 80,
                    'description': 'Be fast, blabla'
                    }
    resp = {'id': 'OD32000115', 'status': 'Success'}
    return jsonify(resp)


@admin_bp.route('/courses', methods=['GET'])
@admin_bp.route('/courses/<id>', methods=['GET'])
def courses(id=None):
    resp = {}
    if not id:
        all_courses = course.Course.query.all()
        resp['count'] = len(all_courses)
        courses = []
        for c in all_courses:
            tmp = {}
            tmp['min_fee'] = c.min_fee
            tmp['id'] = c.id
            tmp['name'] = c.name
            tmp['desc'] = c.desc
            courses.append(tmp)
        resp['items'] = courses
    else:
        c = course.Course.query.filter_by(id=id).first()
        resp['min_fee'] = c.min_fee
        resp['name'] = c.name
        resp['desc'] = c.desc
        resp['books'] = c.books

    return jsonify(resp)


@admin_bp.route('/courses', methods=['POST'])
def create_courses():
    request_body = {'name': 'Psychology', 'min_fee': 80,
                    'description': 'asodi sdjka jlsd  jxkuut ms djksd'
                    }

    name = request_body.get('name', None)
    desc = request_body.get('description', None)
    min_fee = request_body.get('min_fee', None)
    c = course.Course(name=name, desc=desc, min_fee=min_fee)
    textbooks = request.form.getlist('textbooks', None)
    n = 1
    file_key = 'cover-{0}'

    if textbooks:
        for book in textbooks:
            b = course.TextBook(book['name'], book['description'])
            img = request.files.get(file_key.format(n), None)

            if img and not img.filename == '':
                img_path = fileoperation.save_file(img, subfolder='covers')
                img_tmp = image.Image(img_path)
                b.save(img_tmp)

            n += 1
            c.books.append(b)
    try:
        db.session.add(c)
        db.session.commit()
        resp = {'code': 1, 'status': 'Success'}
    except e:
        db.session.rollback()
        resp = {'code': 2, 'status': 'Failure', 'message': repr(e)}

    return jsonify(resp)


@admin_bp.route('/courses/<id>', methods=['POST'])
def edit_course(id):
    request_body = {'id': '2', 'name': 'Psychology',
                    'min_fee': 80,
                    'description': 'asodi sdjka jlsd  jxkuut ms djksd'
                    }
    db.session.begin()
    the_course = course.Course.query.filter(id=id)

    for key, value in request_body.items():
        if not value:
            continue
        the_course[key] = value

    try:
        db.session.add(the_course)
        db.session.commit()
        resp = {'code': 1, 'status': 'Success'}
    except e:
        db.session.rollback()
        resp = {'code': 2, 'status': 'Failure', 'message': repr(e)}

    return jsonify(resp)


@admin_bp.route('/courses/<id>/textbooks', methods=['POST'])
def add_books(course_name):
    request = {'textbooks': ['long', 'kexi']}
    the_course = course.Course.query.filter(id=id).first()
    books = request.form.getlist('textbooks', None)
    file_key = 'cover-{0}'
    n = 0
    for book in books:
        b = course.TextBook(book)
        img = request.files[file_key.format(n)]

        if not img.filename == '':
            img_path = fileoperation.save_file(img, subfolder='answers')
            img_tmp = image.Image(img_path)
            b.save(img_tmp)

        n += 1
        the_course.books.append(b)

        db.session.add(the_course)
    try:
        db.session.commit()
        resp['code'] = 1
        resp['status'] = 'Success'
    except:
        resp['code'] = 2
        resp['status'] = 'Failure'

    return jsonify(resp)


@admin_bp.route('/users', methods=['GET'])
def users():
    resp = {'count': 4, 'items': [{'username': 'dajibaliang',
                                   'type': 'cs', 'permission': 2,
                                   'gender': u'男生',
                                   'email': 'dajibaliang@163.com'},
                                  {'username': 'zhangbiaozi',
                                   'type': 'cs', 'permission': 3,
                                   'gender': u'男生',
                                   'email': 'zhangbiaozi@163.com'},
                                  {'username': 'wangerbiao',
                                  'type': 'customer', 'permission': 0,
                                  'gender': u'男生',
                                   'email': 'wangerbiao@163.com'},
                                  {'username': 'ganniniang',
                                  'type': 'tutor', 'permission': 1,
                                  'gender': u'男生',
                                   'email': 'ganniniang@163.com'}]}

    return jsonify(resp)


@admin_bp.route('/textbooks/<id>/answers', methods=['POST'])
def add_answer(id):
    pass

############# Only For Debug ################################


@admin_bp.route('/')
def home():
    return admin_bp.send_static_file('order_management.html')


@admin_bp.route('/test', methods=['POST', 'GET'])
def forms():
    d = request.form.getlist('step[]')
    print d
    f = request.files
    print f['step[0][picture]'].save('/home/elc/tmp')
    return repr(f)
