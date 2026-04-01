import requests


def opensky():
    url = "https://opensky-network.org/api/states/all"

    planes = requests.get(url).json()

    for i in planes["states"][:10]:
        icao24 = i[0]
        callsign = i[1]
        country = i[2]
        lat = i[6]
        long = i[5]
        alt = i[7]
        print(f"Plane {icao24} {callsign} from {country} at {lat}, {long}, {alt}")