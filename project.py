from qgis.core import QgsProject, QgsMapLayer
from qgis.utils import iface

# List all layers in the project
layers = QgsProject.instance().mapLayers().values()
print(f"Number of layers: {len(layers)}")

for layer in layers:
    if layer.type() == QgsMapLayer.VectorLayer:
        print (f"Vector layer: {layer.name()}")

# Search for a layer by name
communesLayer = None
for layer in QgsProject.instance().mapLayers().values():
    if layer.name() == "communes":
        communesLayer = layer
        break
print (communesLayer.name())

# Zoom to a layer
iface.mapCanvas().setExtent(layer.extent())
iface.mapCanvas().refresh()

# Remove all layers
QgsProject.instance().removeAllMapLayers()

# Save project
QgsProject.instance().write("C:/Users/Salah/Downloads/formation_python_qgis.qgs")