import os

from flask import Flask, render_template

app = Flask(__name__)
page_folder = os.path.join('..', os.path.dirname(__file__), 'pages')
app.static_folder = os.path.join('..', os.path.dirname(__file__), 'src')


def _get_page(pageName: str):
    with open(os.path.join(f"{page_folder}", f"{pageName}.html")) as f:
        return f.read()


@app.route("/")
def root():
    return _get_page('home')


if __name__ == "__main__":
    app.run(debug=False)
