from answerkiller import db


class Solving(db.Model):
     """docstring for Solving"""
     __tablename__ = 'solving_table'
    tutor_username = db.Column(db.ForeignKey('tutors.username'), primary_key=True)
    order_id = db.Column(db.ForeignKey('orders.id'), primary_key=True)
    created_at = db.Column(db.Datetime)
    deadline = db.Column(db.Datetime)
    last_update = db.Column(db.Datetime)
    actual_hours = db.Column(db.Float)
    status = db.Column(db.String(40))
    tutor = db.relationship("Tutor", backref='solving')


class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), primary_key=True)
    nickname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    intro = db.Column(db.String(120))
    gender = db.Column(db.String(10))
    password = db.Column(db.String(120))
    type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_identity':'account',
        'polymorphic_on':type
    }

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Account %r>' % self.username


class Customer(Account):
    __tablename__ = 'customers'
    username = db.Column(db.String(80),  db.ForeignKey('accounts.username'),
                    primary_key=True)   
    school = db.Column(db.String(120))
    grade = db.Column(db.String(20))
    balance = db.Column(db.Float)
    orders = relationship()

    __mapper_args__ = {
        'polymorphic_identity':'customer',
    }

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Customer %r>' % self.username



class CustomerSupport(Account):
    __tablename__ = 'customer_supports'
    username = db.Column(db.String(80),  db.ForeignKey('accounts.username'),
                    primary_key=True)
    permission_level = db.Column(db.Integer)
    orders = relationship()

    __mapper_args__ = {
        'polymorphic_identity':'cs',
    }

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<CustomerSupport %r>' % self.username

class Tutor(Account):
    __tablename__ = 'tutors'
    username = db.Column(db.String(80), db.ForeignKey('accounts.username'),
                    primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'tutor',
    }

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Tutor %r>' % self.username