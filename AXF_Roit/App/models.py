from App.ext import db


class Home(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(32))
    trackid = db.Column(db.Integer,default=1)


    __abstract__ = True

class HomeWheel(Home):

    __tablename__ = 'axf_wheel'


class HomeNav(Home):
    __tablename__ = 'axf_nav'


class HomeMustBuy(Home):
    __tablename__ = 'axf_mustbuy'


class HomeShop(Home):
    __tablename__ = 'axf_shop'