import requests

def get_location():
  """
  Gets the longitude and latitude of the user's current location using their IP address.

  Returns:
    A tuple containing the latitude and longitude as floats, or None if the location
    cannot be determined.
  """
  try:
    response = requests.get("http://ip-api.com/json/")
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    latitude = data.get("lat")
    longitude = data.get("lon")
    if latitude is not None and longitude is not None:    #si latitud es algo y si longitud es algo
      return latitude, longitude
    else:
      return None
  except requests.exceptions.RequestException as e:
    print(f"Error getting location: {e}")
    return None

if __name__ == "__main__":
  location = get_location()
  if location:
    latitude, longitude = location
    print(f"Latitude: {latitude}, Longitude: {longitude}")
  else:
    print("Unable to determine location.")