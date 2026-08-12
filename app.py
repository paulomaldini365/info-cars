from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    cars = [
        {
            "brand": "Porsche",
            "model": "Panamera Turbo S E-Hybrid",
            "year": 2023,
            "engine": "4.0L V8 + Motor Elektrik (PHEV)",
            "power": "700 HP",
            "consumption_100": "2.7 L benzinë + 23.7 kWh (Bateri e plotë)",
            "consumption_1000": "~102 L benzinë (Rrugë e gjatë / Bateri e shkarkuar)",
            "price": "€190,000",
            "image": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "brand": "Audi",
            "model": "S7 Sportback",
            "year": 2022,
            "engine": "3.0L V6 TDI Diesel",
            "power": "344 HP",
            "consumption_100": "7.1 L / 100 km",
            "consumption_1000": "71 L / 1000 km",
            "price": "€85,000",
            "image": "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?auto=format&fit=crop&w=800&q=80"
        },
        {
            "brand": "BMW",
            "model": "330e xDrive",
            "year": 2023,
            "engine": "2.0L Turbo + Motor Elektrik (PHEV)",
            "power": "292 HP",
            "consumption_100": "1.8 L benzinë + 16 kWh (Bateri e plotë)",
            "consumption_1000": "~72 L benzinë (Rrugë e gjatë / Bateri e shkarkuar)",
            "price": "€58,000",
            "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=800&q=80"
        }
    ]
    return render_template('index.html', cars=cars)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
