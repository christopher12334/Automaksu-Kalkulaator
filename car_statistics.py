from flask import Flask, render_template
import folium
import os

app = Flask(__name__)

# Funktsioon, mis loob kaardi ja salvestab selle HTML-failina
def create_map():
    m = folium.Map(location=[50, 10], zoom_start=4)

    # Andmed iga riigi kohta
    tax_data = {
        "Belgium": [50.85, 4.35, 2892],
        "Finland": [60.17, 24.94, 2723],
        "Ireland": [53.35, -6.26, 2438],
        "Austria": [48.21, 16.37, 2409],
        "Denmark": [55.67, 12.56, 2217],
        "Netherlands": [52.37, 4.90, 2160],
        "Germany": [52.52, 13.40, 1764],
        "Italy": [41.90, 12.49, 1727],
        "France": [48.85, 2.35, 1625],
        "Sweden": [59.33, 18.06, 1543],
        "Portugal": [38.72, -9.14, 1290],
        "Greece": [37.98, 23.72, 1264],
        "Spain": [40.42, -3.70, 1148]
    }

    # Lisame iga riigi kaardile
    for country, data in tax_data.items():
        folium.CircleMarker(
            location=[data[0], data[1]],
            radius=data[2] / 1000,  # Suuruse skaleerimine
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.6,
            popup=f"{country}: €{data[2]}"
        ).add_to(m)

    map_path = "static/car_map.html"
    m.save(map_path)
    return map_path

@app.route('/')
def index():
    map_path = create_map()
    return render_template("car_tax_dashboard.html", map_path=map_path)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
