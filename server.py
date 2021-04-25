from flask import Flask
from flask import request, Response
from flask import url_for, redirect, templating
from flask_cors import CORS
from scraping import scrap

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/api/scrap")
def route():
    result_scraping = scrap()
    if request.method == "GET":
        return {
            "message": "Welcome Peeps!",
            "data": result_scraping
        }, 200


@app.errorhandler(404)
def error_not_found(e):
    return {
        "message": "sorry, we can't find the route."
    }, 404


if __name__ == "__main__":
    app.run()
