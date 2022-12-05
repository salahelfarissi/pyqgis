from qgis.core import QgsVectorLayer, QgsProject
import pathlib

# Import the layer
layer = QgsVectorLayer(
    f"{pathlib.Path().resolve()}/GitHub/pyqgis/data/africa/africa.shp", "afrique", "ogr"
)

# Add the layer to the map
QgsProject.instance().addMapLayer(layer)

# Remove the layer from the map
QgsProject.instance().removeMapLayer(layer.id())