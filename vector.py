from qgis.core import QgsVectorLayer, QgsProject

# Import the layer
layer = QgsVectorLayer("C:/Users/Salah/Documents/GitHub/pyqgis/data/Affrique.shp", "afrique", "ogr")

# Add the layer to the map
QgsProject.instance().addMapLayer(layer)