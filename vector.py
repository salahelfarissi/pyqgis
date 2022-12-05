from qgis.core import QgsVectorLayer, QgsProject
import pathlib

# Import the layer
layer = QgsVectorLayer(
    f"{pathlib.Path().resolve()}/GitHub/pyqgis/data/Affrique.shp", "afrique", "ogr"
)

# Add the layer to the map
QgsProject.instance().addMapLayer(layer)

# Remove the layer from the map
# QgsProject.instance().removeMapLayer(layer.id())

# Retrieve data from WFS
from urllib.parse import urlencode, quote_plus

bbox = "48.8461215757, 2.33962949590, 48.8481321430, 2.346401471985"

# Building
params = {
    "service": "WFS",
    "request": "GetFeature",
    "typeName": "BDTOPO_V3:batiment",
    "version": "2.0.0",
    "srsName": "EPSG:2154",
    "outputFormat": "json",
    "BBOX": bbox,
}

urlBati = "https://wxs.ign.fr/topographie/geoportail/wfs?" + urlencode(params, quote_via=quote_plus)
buildLayer = QgsVectorLayer(urlBati, "Bati", "ogr")

# print (batiLayer.featureCount())
QgsProject.instance().addMapLayer(buildLayer)
