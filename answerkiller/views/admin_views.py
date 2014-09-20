# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, jsonify, \
    redirect, url_for, helpers
from flask.ext.login import login_required
from answerkiller.models import course, user, image, order
from answerkiller.utils import fileoperation
from answerkiller import db


admin_bp = Blueprint('Admin', __name__,
                     template_folder='../templates/admin',
                     static_folder='../templates/admin',
                     static_url_path='')


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
        books = []
        for cb in c.books:
          tmp = {}
          tmp['name'] = cb.name
          tmp['id'] = cb.id
          books.append(tmp)
        resp['books'] = books

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


@admin_bp.route('/courses/<cid>', methods=['POST'])
def edit_course(cid):
    request_body = {'name': 'Methodology',
                    'min_fee': 80.3,
                    'description': 'asodi sdjka jlsd  jxkuut ms djksd'
                    }
    the_course = course.Course.query.with_for_update(read=True).filter_by(id=cid)

    for key, value in request_body.items():
        if not value:
            request_body.pop(key)
    result = the_course.update(request_body)
    try:
        db.session.commit()
        resp = {'code': 1, 'status': 'Success',
                'message': 'modified %d' % result}
    except e:
        db.session.rollback()
        resp = {'code': 2, 'status': 'Failure', 'message': repr(e)}

    return jsonify(resp)


@admin_bp.route('/courses/<id>/textbooks', methods=['POST'])
def add_books(id):
    request = {'textbooks': ['long', 'kexi']}
    the_course = course.Course.query.with_for_update(read=True).filter_by(id=id).first()
    books = request.form.getlist('textbooks', None)
    file_key = 'cover-{0}'
    
    n = 0
    for book in books:
        b = course.TextBook(book)
        img = request.files[file_key.format(n)]

        if not img.filename == '':
            img_path = fileoperation.save_file(img, subfolder='covers')
            img_tmp = image.Image(img_path)
            b.save(img_tmp)

        n += 1
        the_course.books.append(b)

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
    resp = {}
    all_users = user.Account.query.all()
    ulist = []
    for u in all_users:
      tmp = {}
      tmp['username'] = u.username
      tmp['email'] = u.email
      tmp['type'] = u.type
      tmp['gender'] = u.gender
      tmp['permission'] = u.permission
      ulist.append(tmp)

    resp['count'] = len(ulist)
    resp['items'] = ulist
    return jsonify(resp)


@admin_bp.route('/textbooks/<id>/answers', methods=['POST'])
def add_answer(id):
    resp = {'code': 1, 'status': 'Success', 'message': "Added Answer"}
    request_body = {'book_id': 1, 'course_id': 2, 'chapter': 10,
                    'qno': 5, 'page': 30, 'content': 'basess'}
    queston = course.Question(request_body['chapter'], request_body['qno'],
                              request_body['page'])
    book = course.TextBook.query.filter_by(id=request_body['book_id']).first()
    print book
    book.questions.append(queston)
    db.session.commit()
    return jsonify(resp)



@admin_bp.route('/questions', methods=['GET'])
def questions():
  resp = {}
  all_questions = course.Question.query.all()
  qlist = []
  for q in all_questions:
    tmp = {
        'id': q.id,
        'book_id': q.book_id,
        'chapter':q.chapter,
        'qno':q.qno,
        'page':q.page
    }
    qlist.append(tmp)
  resp['items'] = qlist
  return jsonify(resp)

############# Only For Debug ################################


@admin_bp.route('/')
def home():
    return admin_bp.send_static_file('order_management.html')


@admin_bp.route('/test', methods=['POST', 'GET'])
def forms():
    d = request.form
    print d
    fs = request.files
    s = []
    print fs
    return '<p><strong>long</strong></p>long'

@admin_bp.route('/login', methods=['POST'])
def login():
  return 'Login Success'