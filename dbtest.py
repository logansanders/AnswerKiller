from answerkiller import app, db
def test_append():
    from answerkiller.models import course, order, user, image
    c = course.Course.query.filter_by(id=1).first()
    book = course.TextBook('sceinece Math')
    #img =image.Image('sssss.jpg')
    #customer = user.Customer('logansanderddd', 'xxx@111.2com', 'sdsd')
    #o = order.Order('test order')
    #book.image= img
    #c.books.append(book)
    #db.session.add(c)
    #db.session.add()
    #db.session.commit()
    for co in db.session.query(course.Course).all():
        for b in co.books:
            print b.image
    #print db.session.query(course.TextBook).first().course
    #print db.session.query(user.Account).first().type
    #print db.session.query(order.Order).first()

#test_append()