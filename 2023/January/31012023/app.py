from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/location", methods=["POST"])
def location():
    print(request.get_json())
    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    return "<h1>Location received</h1>"


if __name__ == "__main__":
    app.run(debug=True)
