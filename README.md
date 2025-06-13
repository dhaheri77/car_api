Car API (Flask)

This project provides a simple mock API built with Flask to serve country, brand, and model data for cars. It’s designed for use in car-related chatbot projects or any application that needs a hierarchical car data structure.

⸻

🚗 Features
	•	/api/countries – returns all available car-producing countries
	•	/api/brands?country=CountryName – returns brands for a given country
	•	/api/models?brand=BrandName – returns car models for a given brand

⸻

🧰 Tech Stack
	•	Python 3.x
	•	Flask 3.1.1

⸻

📦 Project Structure

car_api/
├── app.py                      # Flask application
├── countries.json              # List of countries
├── brands_by_country.json     # Brands organized by country
├── models_by_brand.json       # Models organized by brand
├── structured_car_data.json   # Full hierarchy (country → brand → models)
├── requirements.txt
├── .gitignore
└── venv/                      # Local Python virtual environment (excluded from git)


⸻

🚀 How to Run Locally

1. Clone the repository

git clone https://github.com/dhaheri77/car_api.git
cd car_api

2. Set up the virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Start the Flask server

python app.py

Server will run at: http://127.0.0.1:5000

⸻

🧪 API Endpoints

Get all countries

GET /api/countries

Get brands by country

GET /api/brands?country=Japan

Get models by brand

GET /api/models?brand=Toyota


⸻

📄 License

MIT

⸻

👤 Author

Mubarak Al Dhaheri
GitHub: @dhaheri77

Feel free to fork or contribute!
