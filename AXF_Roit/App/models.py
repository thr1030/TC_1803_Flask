from App.ext import db


class Home(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.Integer)
    trackid = db.Column(db.Integer,default=1)

    class Meta:
        abstract = True

class HomeWheel(Home):
    pass
class HomeNav(Home):
    pass
class HomeMustBuy(Home):
    pass
class HomeShop(Home):
    pass
class HomeMainShow(Home):
    pass



class Market(db.Model):
    pass

class Mine(db.Model):
    pass

class Cart(db.Model):
    pass