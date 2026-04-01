import requests
import folium
import time as t


url = "https://opensky-network.org/api/states/all"
m = folium.Map(location=(0, 0), zoom_start=2, tiles="CartoDB Dark_Matter")

planes = requests.get(url).json()

for i in planes["states"][:100]:
    try:
        folium.Marker(
            location=[i[6], i[5]],
            tooltip=i[1] or "N/A",
            popup=f"icao24: {i[0]}, Country: {i[2]}, Altitude: {i[7]}",
            icon=folium.Icon(icon="plane", prefix="fa", color="blue"),
        ).add_to(m)
    except Exception:
        continue
m.save("index.html")
