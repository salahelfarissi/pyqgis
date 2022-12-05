from qgis.core import QgsVectorLayer, QgsProject

# Import csv layer
url = "file:///C:/Users/Salah/Downloads/birds.csv?delimiter=%s&xField=%s&yField=%s&crs=epsg:4326" % (",", "location-long", "location-lat")
csvLayer = QgsVectorLayer(url, "Birds", "delimitedtext")

# Add layer to the map
QgsProject.instance().addMapLayer(csvLayer)