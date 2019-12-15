import folium
import pandas as pd

#open txt file with volcano data
data = pd.read_csv("Volcanoes.txt")

latitude_list = list(data["LAT"])
longitude_list = list(data["LON"])
elevation_list = list(data["ELEV"])

def elevation_color(elevation_list):
    if elevation_list < 2000:
        return "green"
    elif elevation_list > 3000:
        return "red"
    else:
        return "orange"
    


map = folium.Map(location=[48.7767982,-121.8109970], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")


for lt, ln, el in zip(latitude_list, longitude_list, elevation_list):
    fg.add_child(folium.CircleMarker(location=[lt, ln], color= "gray", radius=6,  fill_color=elevation_color(el), popup= str(el) +" m", fill=True, fill_opacity=0.7))
    
#, icon=folium.Icon(color= elevation_color(el))
# for coordinates in [(latitude_list, longitude_list)]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("VolcanoMap.html")