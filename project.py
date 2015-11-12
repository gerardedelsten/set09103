from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
 return render_template('base.html'), 200


@app.route('/teams')
def teams():
 return render_template('teams.html'), 200

@app.route('/standings')
def standings():
 return render_template('standings.html'), 200


if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)

