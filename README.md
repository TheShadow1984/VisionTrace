This Project is using the OpenSky Network API by:

Matthias Schäfer, Martin Strohmeier, Vincent Lenders, Ivan Martinovic and Matthias Wilhelm.
"Bringing Up OpenSky: A Large-scale ADS-B Sensor Network for Research".
In Proceedings of the 13th IEEE/ACM International Symposium on Information Processing in Sensor Networks (IPSN), pages 83-94, April 2014.

The OpenSky Network, https://opensky-network.org


import requests

# OpenSky REST API
url = "https://opensky-network.org/api/states/all"

response = requests.get(url).json()

# Daten abrufen und nur die ersten 10 Flugzeuge ausgeben
for plane in response['states'][:10]:
    icao24 = plane[0]
    callsign = plane[1].strip() if plane[1] else "N/A"
    lon = plane[5] if plane[5] is not None else "N/A"
    lat = plane[6] if plane[6] is not None else "N/A"
    print(f"Plane {callsign} ({icao24}) at ({lat}, {lon})")