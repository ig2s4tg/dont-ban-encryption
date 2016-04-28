from flask import Flask, render_template, session, redirect, request, url_for
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template

app = Flask(__name__)
Mobility(app)

app.secret_key = 'CHANGE_ME'

### ROUTING ###
@app.route('/', methods=['GET','POST'])
@mobile_template('{mobile/}index.html')
def index(template):
	return render_template(template)

if __name__ == "__main__":
    app.run(debug=True)
