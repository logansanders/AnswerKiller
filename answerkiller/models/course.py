from answerkiller import db
from answerkiller.models import InnoDBMixin


class Course(db.Model, InnoDBMixin):
    """docstring for Course"""
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    min_fee = db.Column(db.Float(precision=2), nullable=False)
    books = db.relationship('TextBook', backref='course')

    def __init__(self, name, min_fee, desc=None):
        self.name = name
        self.min_fee = min_fee
        self.desc = desc

    def __repr__(self):
        return '<Course %r>, min fee %f' % (self.name, self.min_fee)

class TextBook(db.Model, InnoDBMixin):
    """docstring for TextBook"""
    __tablename__ = 'textbooks'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id',
        ondelete="CASCADE"))
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    quetions = db.relationship('Question', backref='textbook')
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<TextBook %r>' % self.name


class Question(db.Model, InnoDBMixin):
    """docstring for Question"""
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('textbooks.id',
        ondelete="CASCADE"))
    chapter = db.Column(db.Integer, nullable=False)
    qno = db.Column(db.Integer, nullable=False)
    page = db.Column(db.Integer, nullable=True)
    content = db.Column(db.Text)
    snapshots = db.Column(db.String(256))
    title = db.Column(db.String(140), nullable=True)
    desc = db.Column(db.Text, nullable=True)
    answers = db.relationship('Answer', backref='question')

    def __init__(self, title):
        self.title = title


class Answer(db.Model, InnoDBMixin):
    """docstring for Answer"""
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id',
        ondelete="CASCADE"))
    text = db.Column(db.Text, nullable=True)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship('Image')
    step = db.Column(db.Integer)

    def __init__(self, step):
        self.step = step

        
        