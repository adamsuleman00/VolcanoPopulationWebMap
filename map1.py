import folium  
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000:
        return '#00cc00'
    elif 1000 <= elevation <3000:
        return '#ff9900'
    else:
        return '#ff0000'

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="stamentoner")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), 
    fill_color=color_producer(el), color = '#787878'))
 
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
 
map.add_child(fg) 

map.save("Map1.html")         