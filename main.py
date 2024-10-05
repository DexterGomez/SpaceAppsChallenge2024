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


#initalizate states
if "my_latitude" not in st.session_state:
  st.session_state.my_latitude = 0
if "my_longitude" not in st.session_state:
  st.session_state.my_longitude = 0
if "zoom_start" not in st.session_state:
  st.session_state.zoom_start = 1

if "coords" in st.session_state and st.session_state.coords != None:
  st.session_state.zoom_start = 6

if st.button("my location"):
  st.session_state.my_latitude, st.session_state.my_longitude = get_location()
  st.session_state.zoom_start = 12

if st.button("go world"):
  st.session_state.my_latitude, st.session_state.my_longitude = 0,0
  st.session_state.zoom_start = 1
  st.session_state.coords = None



# Create a Folium map centered on a default location
m = folium.Map(location=[st.session_state.my_latitude, st.session_state.my_longitude], zoom_start=st.session_state.zoom_start)

# Add a marker at a specific location
folium.Marker(
    location=[st.session_state.my_latitude, st.session_state.my_longitude], # Replace with your desired coordinates
    #popup=f"lat:{st.session_state.my_latitude}\nlong:{st.session_state.my_longitude}",
    #tooltip="Click me!"
    tooltip = f"lat:{st.session_state.my_latitude}, long:{st.session_state.my_longitude}"
).add_to(m)


# Display the map with Streamlit
map = st_folium(m, width=700, height=450)

# Get coordinates if the map was clicked
st.session_state.coords = get_coordinates(map)

if st.session_state.coords:
  st.write(f"Selected coordinates: {st.session_state.coords}")
  st.session_state.my_latitude, st.session_state.my_longitude = st.session_state.coords[0], st.session_state.coords[1]
  print(st.session_state.coords)
  # You can now use the 'coords' variable for further processing
else:
  st.write(f"Selected coordinates: {st.session_state.my_latitude, st.session_state.my_longitude}")


st.write("Made by Edoardo, Jorge Luis, Dexter y Jorge Cyber.")