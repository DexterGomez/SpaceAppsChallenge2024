import streamlit as st                   #librería de la página web
from streamlit_folium import st_folium   #librería de la página web con folium
import folium                            #Librería de geolocalización

from get_location_from_ip import get_location       #Librería dexter para obtener ubicación con IP

st.title("Open Effectiveness UPY: Landsat data tracking platform")

def get_coordinates(map):
  """Retrieves coordinates from the map if a click event occurred."""
  if map.get("last_clicked"):
    return map["last_clicked"]["lat"], map["last_clicked"]["lng"]
  return None

# Create a Folium map centered on a default location
m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Display the map with Streamlit
map = st_folium(m, width=700, height=450)

# Get coordinates if the map was clicked
coords = get_coordinates(map)

if coords:
  st.write(f"Clicked coordinates: {coords}")
  print(coords)
  # You can now use the 'coords' variable for further processing

st.write("Holaa")