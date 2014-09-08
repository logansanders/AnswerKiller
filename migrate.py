from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from answerkiller import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

'''
def test_append():
    from answerkiller.models import course, order, user
    c = course.Course('Math', 50.2)
    book = course.TextBook('Adavance Math')
    #customer = user.Customer('logansanderddd', 'xxx@111.2com', 'sdsd')
    #o = order.Order('test order')
    c.books.append(book)
    #db.session.add(c)
    db.session.add(c)
    db.session.commit()
    for co in db.session.query(course.Course).all():
        print co.books
    #print db.session.query(course.TextBook).first().course
    #print db.session.query(user.Account).first().type
    #print db.session.query(order.Order).first()

test_append()
'''
