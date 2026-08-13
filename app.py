import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Baza e zgjeruar e të dhënave me shumë më tepër modele
CARS_DATA = {
    "Porsche": [
        {
            "model": "Panamera Turbo S",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo Hybrid",
            "power": "700 HP",
            "image": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=800"
        },
        {
            "model": "Taycan Turbo S",
            "year": "2024",
            "engine": "Electric (Dual Motor)",
            "power": "761 HP",
            "image": "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=800"
        },
        {
            "model": "911 GT3 RS",
            "year": "2024",
            "engine": "4.0L Flat-6 Naturally Aspirated",
            "power": "525 HP",
            "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800"
        },
        {
            "model": "Macan GTS",
            "year": "2023",
            "engine": "2.9L V6 Twin-Turbo",
            "power": "440 HP",
            "image": "https://images.unsplash.com/photo-1580273916550-e323be2ae537?w=800"
        },
        {
            "model": "Cayenne Turbo GT",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "659 HP",
            "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800"
        },
        {
            "model": "718 Cayman GT4 RS",
            "year": "2023",
            "engine": "4.0L Flat-6",
            "power": "500 HP",
            "image": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=800"
        }
    ],
    "Audi": [
        {
            "model": "S7 Sportback",
            "year": "2023",
            "engine": "2.9L V6 Twin-Turbo",
            "power": "444 HP",
            "image": "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?w=800"
        },
        {
            "model": "RS7 Sportback Performance",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "630 HP",
            "image": "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?w=800"
        },
        {
            "model": "RS6 Avant",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "600 HP",
            "image": "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?w=800"
        },
        {
            "model": "R8 V10 Performance",
            "year": "2023",
            "engine": "5.2L V10",
            "power": "620 HP",
            "image": "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?w=800"
        },
        {
            "model": "RS Q8",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "600 HP",
            "image": "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?w=800"
        }
    ],
    "BMW": [
        {
            "model": "M5 Competition",
            "year": "2023",
            "engine": "4.4L V8 Twin-Turbo",
            "power": "625 HP",
            "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800"
        },
        {
            "model": "M3 Competition xDrive",
            "year": "2024",
            "engine": "3.0L Inline-6 Twin-Turbo",
            "power": "510 HP",
            "image": "https://images.unsplash.com/photo-1580273916550-e323be2ae537?w=800"
        },
        {
            "model": "M4 CSL",
            "year": "2023",
            "engine": "3.0L Inline-6 Twin-Turbo",
            "power": "550 HP",
            "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800"
        },
        {
            "model": "M8 Competition Coupe",
            "year": "2024",
            "engine": "4.4L V8 Twin-Turbo",
            "power": "625 HP",
            "image": "https://images.unsplash.com/photo-1520050206274-a1ae44613e6d?w=800"
        },
        {
            "model": "X5 M Competition",
            "year": "2024",
            "engine": "4.4L V8 Twin-Turbo",
            "power": "625 HP",
            "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800"
        }
    ],
    "Mercedes-Benz": [
        {
            "model": "AMG GT 63 S 4-Door",
            "year": "2023",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "639 HP",
            "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800"
        },
        {
            "model": "G 63 AMG",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "585 HP",
            "image": "https://images.unsplash.com/photo-1520050206274-a1ae44613e6d?w=800"
        },
        {
            "model": "S 63 AMG E Performance",
            "year": "2024",
            "engine": "4.0L V8 Plug-in Hybrid",
            "power": "802 HP",
            "image": "https://images.unsplash.com/photo-1563720223185-11003d516935?w=800"
        },
        {
            "model": "C 63 S AMG E Performance",
            "year": "2024",
            "engine": "2.0L Turbo Hybrid",
            "power": "680 HP",
            "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800"
        }
    ],
    "Volkswagen": [
        {
            "model": "Golf 8 R",
            "year": "2024",
            "engine": "2.0L Turbo Inline-4",
            "power": "320 HP",
            "image": "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800"
        },
        {
            "model": "Golf GTI Clubsport",
            "year": "2023",
            "engine": "2.0L Turbo Inline-4",
            "power": "300 HP",
            "image": "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800"
        },
        {
            "model": "Arteon R Shooting Brake",
            "year": "2023",
            "engine": "2.0L Turbo Inline-4",
            "power": "320 HP",
            "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800"
        },
        {
            "model": "Touareg R",
            "year": "2024",
            "engine": "3.0L V6 Plug-in Hybrid",
            "power": "462 HP",
            "image": "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800"
        }
    ],
    "Ferrari": [
        {
            "model": "SF90 Stradale",
            "year": "2023",
            "engine": "4.0L V8 Plug-in Hybrid",
            "power": "1000 HP",
            "image": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=800"
        },
        {
            "model": "296 GTB",
            "year": "2024",
            "engine": "3.0L V6 Turbo Hybrid",
            "power": "830 HP",
            "image": "https://images.unsplash.com/photo-1592198084033-aade902d1aae?w=800"
        },
        {
            "model": "Purosangue",
            "year": "2024",
            "engine": "6.5L V12 Naturally Aspirated",
            "power": "725 HP",
            "image": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=800"
        },
        {
            "model": "F8 Tributo",
            "year": "2022",
            "engine": "3.9L V8 Twin-Turbo",
            "power": "720 HP",
            "image": "https://images.unsplash.com/photo-1592198084033-aade902d1aae?w=800"
        }
    ],
    "Lamborghini": [
        {
            "model": "Revuelto",
            "year": "2024",
            "engine": "6.5L V12 Plug-in Hybrid",
            "power": "1015 HP",
            "image": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=800"
        },
        {
            "model": "Huracán STO",
            "year": "2023",
            "engine": "5.2L V10",
            "power": "640 HP",
            "image": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=800"
        },
        {
            "model": "Urus Performante",
            "year": "2024",
            "engine": "4.0L V8 Twin-Turbo",
            "power": "666 HP",
            "image": "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?w=800"
        }
    ],
    "Nissan": [
        {
            "model": "GT-R Nismo",
            "year": "2024",
            "engine": "3.8L V6 Twin-Turbo",
            "power": "600 HP",
            "image": "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=800"
        },
        {
            "model": "Z Performance",
            "year": "2024",
            "engine": "3.0L V6 Twin-Turbo",
            "power": "400 HP",
            "image": "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=800"
        }
    ]
}

@app.route('/')
def home():
    search_query = request.args.get('search', '').strip().lower()
    
    filtered_brands = {}
    if search_query:
        for brand, models in CARS_DATA.items():
            matching_models = [
                car for car in models 
                if search_query in brand.lower() or search_query in car['model'].lower()
            ]
            if matching_models:
                filtered_brands[brand] = matching_models
    else:
        filtered_brands = CARS_DATA

    return render_template('index.html', brands=filtered_brands, search_query=search_query)

@app.route('/brand/<brand_name>')
def brand_page(brand_name):
    cars = CARS_DATA.get(brand_name, [])
    return render_template('brand.html', brand_name=brand_name, cars=cars)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
