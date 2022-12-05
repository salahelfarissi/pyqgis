from qgis.utils import iface
from PyQt5.QtGui import QColor

canvasOverview = iface.createNewMapCanvas("Overview")
canvasOverview.setCanvasColor(QColor.fromRgb(209,242,235))

canvas = iface.mapCanvases()
print(len(canvas))

iface.messageBar().pushSuccess("Success", "Bienvenue dans la formation Python pour QGis")