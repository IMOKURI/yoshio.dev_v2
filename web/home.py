from flask import Blueprint, render_template


BP = Blueprint("home", __name__)


@BP.route("/")
def index():
    return render_template("pages/index.html")
