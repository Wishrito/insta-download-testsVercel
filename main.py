from os.path import dirname, join

from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = join(dirname(__file__), 'pages')
app.static_folder = join(dirname(__file__), 'static')


@app.route("/")
def read_root():
    return render_template('home.html')
