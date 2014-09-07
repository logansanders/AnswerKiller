from answerkiller import db
from answerkiller.models import InnoDBMixin


class Solving(db.Model, InnoDBMixin):
    __tablename__ = 'solving_table'

    tutor_username = db.Column(db.ForeignKey('tutors.username'), primary_key=True)
    order_id = db.Column(db.ForeignKey('orders.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    created_at = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    last_update = db.Column(db.DateTime)
    actual_hours = db.Column(db.Float)
    status = db.Column(db.String(40))
    tutor = db.relationship("Tutor", backref='solving')


class Account(db.Model, InnoDBMixin):
    __tablename__ = 'accounts'

    username = db.Column(db.String(80), primary_key=True)
    nickname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    intro = db.Column(db.String(120))
    gender = db.Column(db.String(10))
    password = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_identity':'account',
        'polymorphic_on':type
    }

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Account %r>' % self.username


class Customer(Account):
    __tablename__ = 'customers'

    username = db.Column(db.String(80),  db.ForeignKey('accounts.username'),
        primary_key=True)   
    school = db.Column(db.String(120))
    grade = db.Column(db.String(20))
    balance = db.Column(db.Float)
    orders = db.relationship('Order', backref='owner')

    __mapper_args__ = {
        'polymorphic_identity':'customer',
    }

    def __repr__(self):
        return '<Customer %r>' % self.username


class CustomerSupport(Account):
    __tablename__ = 'customer_supports'

    username = db.Column(db.String(80), db.ForeignKey('accounts.username',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    permission_level = db.Column(db.Integer)
    orders = db.relationship('Order', backref='customer')

    __mapper_args__ = {
        'polymorphic_identity':'cs',
    }

    def __repr__(self):
        return '<CustomerSupport %r>' % self.username


class Tutor(Account):
    __tablename__ = 'tutors'

    username = db.Column(db.String(80), db.ForeignKey('accounts.username',
        onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'tutor',
    }

    def __repr__(self):
        return '<Tutor %r>' % self.username