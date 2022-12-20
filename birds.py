from qgis.core import QgsVectorLayer, QgsProject

# Import csv layer
url = "file:///C:/Users/Salah/Documents/GitHub/pyqgis/data/black-tailed.csv?delimiter=%s&xField=%s&yField=%s&crs=epsg:%s" % (",", "location-long", "location-lat", 4326)
csvLayer = QgsVectorLayer(url, "Birds", "delimitedtext")

# Add countries layer
# countriesLayer = QgsVectorLayer("C:/Users/Salah/Documents/GitHub/pyqgis/data/countries/countries.shp", "Countries", "ogr")

QgsProject.instance().removeAllMapLayers()

# Add layers to the map
# QgsProject.instance().addMapLayer(countriesLayer)
QgsProject.instance().addMapLayer(csvLayer)

# Construct an iterator to iterate over the features of the layer
iterator = csvLayer.getFeatures()

NAMES = []
for feature in iterator:
    featureAttributes = feature.attributes()
    birdName = featureAttributes[26]

    if birdName not in NAMES:
        NAMES.append(birdName)

NAMES.sort()
print(NAMES)

# field_names = [field.name() for field in csvLayer.fields()]
# for field in field_names:
#     print(field)

# Define a subset of the layer
csvLayer.setSubsetString("\"individual-local-identifier\" = 'Amalia'")
for feature in csvLayer.getFeatures():
    print(feature["individual-local-identifier"])