import folium
import pandas as pd

#open txt file with volcano data
data = pd.read_csv("Volcanoes.txt")

latitude_list = list(data["LAT"])
longitude_list = list(data["LON"])
location_list = list(data["NAME"])


map = folium.Map(location=[18.462398, -77.326442], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")


for latitude, longitude, location in zip(latitude_list, longitude_list, location_list):
    fg.add_child(folium.Marker(location=[latitude, longitude], popup="Name: " + location, icon=folium.Icon(color='green')))
    
# for coordinates in [(latitude_list, longitude_list)]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("VolcanoMap.html")