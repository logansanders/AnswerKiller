from answerkiller import db


class Course(db.Model):
    """docstring for Course"""
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    desc = db.Column(db.String(1024), nullable=False)
    min_fee = db.Column(db.Float, nullable=False)
    books = db.relationship()

class TextBook(db.Model):
    """docstring for TextBook"""
    __tablename__ = 'textbooks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    desc = db.Column(db.String(1024), nullable=False)
    quetions = db.relationship()

        
class Question(db.Model):
    """docstring for Question"""
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    book_id = 
    chapter =
    qno = 
    page = 
    content = 
    snapshots = 
    name = db.Column(db.String(1024), nullable=False)
    desc = db.Column(db.String(1024), nullable=False)
    answers = db.Column()

class Answer(db.Model):
    """docstring for Answer"""
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=True)
    question_id = 
    image_id = 
    step = db.Column(db.Integer)


        
        