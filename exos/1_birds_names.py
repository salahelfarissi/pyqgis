from qgis.core import QgsVectorLayer, QgsProject

# Import csv layer
url = "file:///C:/Users/Salah/Documents/GitHub/pyqgis/data/black-tailed.csv?delimiter=%s&xField=%s&yField=%s&crs=epsg:%s" % (",", "location-long", "location-lat", 4326)
csvLayer = QgsVectorLayer(url, "Birds", "delimitedtext")

# Add countries layer
countriesLayer = QgsVectorLayer("C:/Users/Salah/Documents/GitHub/pyqgis/data/countries/countries.shp", "Countries", "ogr")

# Remove all layers from the map
QgsProject.instance().removeAllMapLayers()

# Add layers to the map
QgsProject.instance().addMapLayer(countriesLayer)
QgsProject.instance().addMapLayer(csvLayer)

# Construct an iterator to iterate over the features of the layer
iterator = csvLayer.getFeatures()

# Get list of bird names
featureAttributes = [feature.attributes() for feature in iterator]
NAMES = [featureAttributes[i][26] for i in range(len(featureAttributes))]
NAMES = sorted(list(set(NAMES)))

# Define a subset of the layer
csvLayer.setSubsetString("\"individual-local-identifier\" = 'Amalia'")