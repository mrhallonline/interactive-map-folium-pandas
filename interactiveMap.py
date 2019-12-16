import folium
import pandas as pd

#open txt file with volcano data
data = pd.read_csv("Volcanoes.txt")
#isolate specific columns from txt file
latitude_list = list(data["LAT"])
longitude_list = list(data["LON"])
elevation_list = list(data["ELEV"])

#function changing map color based on elevation range
def elevation_color(elevation_list):
    if elevation_list < 2000:
        return "green"
    elif elevation_list > 3000:
        return "red"
    else:
        return "orange"
    

    
#Starting location when map is opened
map = folium.Map(location=[48.7767982,-121.8109970], zoom_start=6, tiles="Stamen Terrain")

#make a features group so that features can be added 
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

# add GeoJson file
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#adding map markers using long and lat from text file
for lt, ln, el in zip(latitude_list, longitude_list, elevation_list):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], color= "gray", radius=6,  fill_color=elevation_color(el), popup= str(el) +" m", fill=True, fill_opacity=0.7))

#was used when added markers using icons    
#, icon=folium.Icon(color= elevation_color(el))
# for coordinates in [(latitude_list, longitude_list)]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))



# add child to feature group
map.add_child(fgv)
map.add_child(fgp)

# add layer control options
map.add_child(folium.LayerControl())

#create html file
map.save("VolcanoMap.html")