from flask import Blueprint

blue = Blueprint("first_blue",__name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def hello():
    return "Welcom to use Flask!"


@blue.route('/home/')
def home():
    # wheels = HomeWheel.objects.all()
    #
    # navs = HomeNav.objects.all()
    #
    # mustbuys = HomeMustBuy.objects.all()
    #
    # shops = HomeShop.objects.all()
    #
    # shops0_1 = shops[0:1]
    #
    # shops1_3 = shops[1:3]
    #
    # shops3_7 = shops[3:7]
    #
    # shops7_11 = shops[7:11]
    #
    # mainshows = HomeMainShow.objects.all()
    #
    # data = {
    #     'title' : '首页',
    #     "wheels" : wheels,
    #     'navs' : navs,
    #     'mustbuys': mustbuys,
    #     'shops0_1' : shops0_1,
    #     'shops1_3' : shops1_3,
    #     'shops3_7' : shops3_7,
    #     'shops7_11' : shops7_11,
    #     'mainshows' :mainshows,
    # }
    return "data"

