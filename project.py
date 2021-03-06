from flask import Flask, render_template
app = Flask(__name__)
#pages from navbar
@app.route('/')
def home():
 return render_template('base.html'), 200

@app.route('/teams')
def teams():
 return render_template('teams.html'), 200


@app.route('/standings')
def standings():
 return render_template('standings.html'), 200

@app.route('/media')
def media():
 return render_template('media.html'), 200

#404 Error

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# team routing premiership clubs
@app.route('/teams/aberdeen/')
def aberdeen():
 return render_template('/teams/aberdeen.html'), 200

@app.route('/teams/celtic/')
def celtic():
 return render_template('/teams/celtic.html'), 200

@app.route('/teams/dundee/')
def dundee():
 return render_template('/teams/dundee.html'), 200

@app.route('/teams/dundee_united/')
def dundee_united():
 return render_template('/teams/dundee_united.html'), 200

@app.route('/teams/hamilton/')
def hamilton():
 return render_template('/teams/hamilton.html'), 200

@app.route('/teams/hearts/')
def hearts():
 return render_template('/teams/hearts.html'), 200

@app.route('/teams/inverness/')
def inverness():
 return render_template('/teams/inverness.html'), 200

@app.route('/teams/kilmarnock/')
def kilmarnock():
 return render_template('/teams/kilmarnock.html'), 200

@app.route('/teams/motherwell/')
def motherwell():
 return render_template('/teams/motherwell.html'), 200

@app.route('/teams/partick_thistle/')
def partick_thistle():
 return render_template('/teams/partick_thistle.html'), 200

@app.route('/teams/ross_county/')
def ross_county():
 return render_template('/teams/ross_county.html'), 200


@app.route('/teams/stjohnstone/')
def stjohnstone():
 return render_template('/teams/stjohnstone.html'), 200

#champtionship clubs

@app.route('/teams/alloa/')
def alloa():
 return render_template('/teams/alloa.html'), 200

@app.route('/teams/dumbarton/')
def dumbarton():
 return render_template('/teams/dumbarton.html'), 200

@app.route('/teams/falkirk/')
def falkirk():
 return render_template('/teams/falkirk.html'), 200

@app.route('/teams/hibernian/')
def hibernian():
 return render_template('/teams/hibernian.html'), 200

@app.route('/teams/livingston/')
def livingston():
 return render_template('/teams/livingston.html'), 200


@app.route('/teams/morton/')
def morton():
 return render_template('/teams/morton.html'), 200

@app.route('/teams/queen_ots/')
def queen_ots():
 return render_template('/teams/queen_ots.html'), 200

@app.route('/teams/raith_rovers/')
def raith_rovers():
 return render_template('/teams/raith_rovers.html'), 200

@app.route('/teams/rangers/')
def rangers():
 return render_template('/teams/rangers.html'), 200

@app.route('/teams/stmirren/')
def stmirren():
 return render_template('/teams/stmirren.html'), 200

#league one clubs

@app.route('/teams/airdrieonians/')
def airdrieonians():
 return render_template('/teams/airdrieonians.html'), 200

@app.route('/teams/albion_rovers/')
def albion_rovers():
 return render_template('/teams/albion_rovers.html'), 200

@app.route('/teams/ayr_united/')
def ayr_united():
 return render_template('/teams/ayr_united.html'), 200

@app.route('/teams/brechin_city/')
def brechin_city():
 return render_template('/teams/brechin_city.html'), 200

@app.route('/teams/cowdenbeath/')
def cowdenbeath():
 return render_template('/teams/cowdenbeath.html'), 200

@app.route('/teams/dunfermline/')
def dunfermline():
 return render_template('/teams/dunfermline.html'), 200

@app.route('/teams/forfar_athletic/')
def forfar_athletic():
 return render_template('/teams/forfar_athletic.html'), 200

@app.route('/teams/peterhead/')
def peterhead():
 return render_template('/teams/peterhead.html'), 200

@app.route('/teams/stenhousemuir/')
def stenhousemuir():
 return render_template('/teams/stenhousemuir.html'), 200

@app.route('/teams/stranraer/')
def stranraer():
 return render_template('/teams/stranraer.html'), 200

#league two clubs

@app.route('/teams/annan_athletic/')
def annan():
 return render_template('/teams/annan_athletic.html'), 200

@app.route('/teams/arbroath/')
def arbroath():
 return render_template('/teams/arbroath.html'), 200

@app.route('/teams/berwick_rangers/')
def berwick_rangers():
 return render_template('/teams/berwick_rangers.html'), 200

@app.route('/teams/clyde/')
def clyde():
 return render_template('/teams/clyde.html'), 200

@app.route('/teams/east_fife/')
def east_fife():
 return render_template('/teams/east_fife.html'), 200

@app.route('/teams/east_stirling/')
def east_stirling():
 return render_template('/teams/east_stirling.html'), 200

@app.route('/teams/elgin_city/')
def elgin_city():
 return render_template('/teams/elgin_city.html'), 200

@app.route('/teams/montrose/')
def montrose():
 return render_template('/teams/montrose.html'), 200

@app.route('/teams/queens_park/')
def queens_park():
 return render_template('/teams/queens_park.html'), 200

@app.route('/teams/stirling_albion/')
def stirling_albion():
 return render_template('/teams/stirling_albion.html'), 200


if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views
