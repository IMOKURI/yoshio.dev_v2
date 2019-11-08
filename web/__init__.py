from flask import Flask, render_template

from web import home

APP = Flask(__name__)
APP.register_blueprint(home.BP)


@APP.errorhandler(404)
def error_not_found(_):
    return render_template("errors/404.html"), 404
