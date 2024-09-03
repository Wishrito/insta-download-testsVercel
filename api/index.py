from flask import Flask, render_template
import os

app = Flask(__name__)
app.template_folder = os.path.join('..', os.path.dirname(__file__), 'pages')
app.static_folder = os.path.join('..', os.path.dirname(__file__), 'src')


@app.route("/")
def read_root():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=False)
