from qgis.core import QgsVectorLayer, QgsProject

# Import csv layer
url = "file:///C:/Users/Salah/Documents/GitHub/pyqgis/data/birds.csv?delimiter=%s&xField=%s&yField=%s&crs=epsg:4326" % (",", "location-long", "location-lat")
csvLayer = QgsVectorLayer(url, "Birds", "delimitedtext")

# Add countries layer
countriesLayer = QgsVectorLayer("C:/Users/Salah/Documents/GitHub/pyqgis/data/countries/countries.shp", "Countries", "ogr")

# Add layers to the map
QgsProject.instance().addMapLayer(countriesLayer)
QgsProject.instance().addMapLayer(csvLayer)