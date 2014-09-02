from answerkiller import db


class Question(db.Model):
    description = db.Column()
    course = db.Column()
    pno = db.Column()
    qid = db.Column()