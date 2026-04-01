import requests
import folium

# API abfragen
url = "https://opensky-network.org/api/states/all"
response = requests.get(url)
data = response.json()

# Karte initialisieren
m = folium.Map(location=[0, 0], zoom_start=2)

# Flugzeuge als Marker hinzufügen
for plane in data['states'][:50]:  # nur die ersten 50
    if plane[5] is not None and plane[6] is not None:
        callsign = plane[1].strip() if plane[1] else "N/A"
        folium.Marker(
            location=[plane[6], plane[5]],
            tooltip=f"{callsign} ({plane[0]})"
        ).add_to(m)

# Karte speichern
m.save("flugzeuge.html")
print("Karte erstellt: flugzeuge.html")