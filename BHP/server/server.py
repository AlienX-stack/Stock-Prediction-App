from webbrowser import get

from flask import Flask, jsonify, request

import util

app = Flask(__name__)


@app.route("/get_location_names")
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/get_estimated_price", methods=["POST"])
def get_estimated_price():
    total_sqft = float(request.form["total_sqft"])
    bath = int(request.form["bath"])
    bhk = int(request.form["bhk"])
    location = request.form["location"]
    response = jsonify(
        {"estimated_price": util.get_estimated_price(location, total_sqft, bath, bhk)}
    )

    return response


if __name__ == "__main__":
    # app.run(debug=True)
    print("Starting Pyhton Flask Server...")
    util.load_saved_artifacts()
    app.run()

