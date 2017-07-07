from flask import Flask, render_template, \
	url_for
from calendario import monta_calendario

app = Flask(__name__)


@app.route('/')
def index():

	return render_template('index.html',
		calendario=monta_calendario())