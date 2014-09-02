from answerkiller import db


class Answer(db.Model):
    aid = db.Column()
    img_path = db.Column()
    img_no = db.Column()
    qid = db.Column()