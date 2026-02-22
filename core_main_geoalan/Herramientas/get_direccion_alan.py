from geopy.geocoders import Nominatim

def get_direccion_alancore(lat: str, lon: str):
    geolocator = Nominatim(user_agent="alan")
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.address
    

