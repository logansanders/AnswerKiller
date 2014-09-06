from answerkiller import db


class Image(db.Model):
    """docstring for Image"""
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(1024), primary_key=True)

    def __init__(self, path):
        self.path = path