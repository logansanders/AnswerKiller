from answerkiller import db


class User(db.Model):
    """docstring for User"""
    username = db.Column()
    ps_hash = db.Column()
