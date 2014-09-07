from answerkiller import db
from answerkiller.models import InnoDBMixin


class Order(db.Model, InnoDBMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.ForeignKey('customers.username'))
    cs_id = db.Column(db.ForeignKey('customer_supports.username'))
    status = db.Column(db.String(40))
    created_at = db.Column(db.DateTime)
    last_update = db.Column(db.DateTime)
    dealine = db.Column(db.DateTime)
    descr = db.Column(db.Text)
    amount = db.Column(db.Float)
    prepay = db.Column(db.Float)
    name = db.Column(db.String(60))
    tutors = db.relationship('Solving', backref='order')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Order %r>' % self.name