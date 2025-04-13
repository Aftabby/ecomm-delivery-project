from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, from Flask!"


@app.route("/ecomm-delivery")
def ecomm_delivery():
    context = {
        "sample_table": load_sample().head().to_html(index=False),
        "graph_json": graph(),
    }

    return render_template("project3.html", conntext=context)


if __name__ == "__main__":
    app.run(
        debug=True
    )  # ! IMPORTANT: Remove "debug=True" before deploying to production, though using wsgi.py for Gunicorn is the best practice.
