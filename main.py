import requests
import folium
import time as t


url = "https://opensky-network.org/api/states/all"
m = folium.Map(location=(0, 0), zoom_start=2, tiles="CartoDB Dark_Matter")

planes = requests.get(url).json()

for i in planes["states"][:10]:
    icao24 = i[0]
    callsign = i[1]
    country = i[2]
    lat = i[6]
    long = i[5]
    alt = i[7]
    try:
        folium.Marker(
            location=[lat, long],
            tooltip=callsign ,
            popup=f"icao24: {icao24}, country: {country}, altitude: {alt}",
            icon=folium.Icon(icon="plane", prefix="fa", color="blue"),
        ).add_to(m)
    except Exception:
        continue
