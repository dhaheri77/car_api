from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("countries.json") as f:
    countries = json.load(f)

with open("brands_by_country.json") as f:
    brands_by_country = json.load(f)

with open("models_by_brand.json") as f:
    models_by_brand = json.load(f)

@app.route("/api/countries")
def get_countries():
    return jsonify(countries)

@app.route("/api/brands")
def get_brands():
    country = request.args.get("country")
    return jsonify(brands_by_country.get(country, []))

@app.route("/api/models")
def get_models():
    brand = request.args.get("brand")
    return jsonify(models_by_brand.get(brand, []))

@app.route('/')
def index():
    return jsonify({"message": "Car API is running!"})

if __name__ == "__main__":
    app.run(debug=True)