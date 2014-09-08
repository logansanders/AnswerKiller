# -*- coding: utf-8 -*-
from answerkiller import db
from answerkiller.models import InnoDBMixin
import datetime

class Order(db.Model, InnoDBMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.ForeignKey('customers.username'))
    cs_id = db.Column(db.ForeignKey('customer_supports.username'))
    status = db.Column(db.Enum('Completed', 'Created', 'Paid', 'Processing'))
    created_at = db.Column(db.DateTime)
    last_update = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    descr = db.Column(db.Text)
    amount = db.Column(db.Float(precision=2))
    prepay = db.Column(db.Float(precision=2))
    name = db.Column(db.String(60))
    course = db.Column(db.String(80))
    tutors = db.relationship('Solving', backref='order')

    def __init__(self, name, course, deadline, amount, desc=None):
        self.name = name
        self.created_at = datetime.datetime.now()
        self.deadline = deadline
        self.amount = amount
        self.desc = desc

    def __repr__(self):
        return '<Order %r>' % self.name


class AccountRecord(db.Model, InnoDBMixin):
    """docstring for TransactionRecord"""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(precision=2), nullable=False)
    account_balance = db.Column(db.Float(precision=2), nullable=False)
    descr = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, amount, account_balance, desc=None):
        self.amount = amount
        self.account_balance = account_balance
        self.desc = desc
        self.created_at = datetime.datetime.now()
        