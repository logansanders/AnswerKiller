from answerkiller import db


class Order(db.Model):
     """docstring for Order"""
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.ForeignKey('customers.username'))
    cs_id = db.Column(db.ForeignKey('customer_supports.username'))
    status = db.Column(db.String(40))
    created_at = db.Column(db.Datetime)
    last_update = db.Column(db.Datetime)
    dealine = db.Column(db.Datetime)
    descr = db.Column(db.String(1024))
    amount = db.Column(db.Float)
    prepay = db.Column(db.Float)
    name = db.Column(db.String(256))
    tutors = db.relationship('Solving', backref='order')
