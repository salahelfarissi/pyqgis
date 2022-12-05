from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem, QgsCoordinateTransform

# Define the source and destination CRS
sourceCrs = QgsCoordinateReferenceSystem("EPSG:4326")
destinationCrs = QgsCoordinateReferenceSystem("EPSG:3857")

# Create a coordinate transform
transform = QgsCoordinateTransform(sourceCrs, destinationCrs, QgsProject.instance())

# Read a csv file
url = "file:///C:/Users/Salah/Documents/GitHub/pyqgis/data/black-tailed.csv?delimiter=%s&xField=%s&yField=%s&crs=epsg:4326" % (",", "location-long", "location-lat")
csvLayer = QgsVectorLayer(url, "Birds", "delimitedtext")

for feature in csvLayer.getFeatures():
    # Get the geometry of the feature
    geometry = feature.geometry()
    
    # Transform the geometry
    geometry.transform(transform)