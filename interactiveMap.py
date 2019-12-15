import folium

map = folium.Map(location=[18.462398, -77.326442], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[18.462398, -77.326442], [17.462398, -77.326442], [15.462398, -77.326442], [13.462398, -77.326442]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[17.462398, -77.326442], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[15.462398, -77.326442], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")