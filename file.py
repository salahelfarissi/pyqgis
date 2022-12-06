from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsField, QgsPointXY, QgsFeature, QgsGeometry
from sklearn.cluster import DBSCAN
import numpy as np
from PyQt5.QtCore import QVariant

# Import csv layer
url = "file:///C:/Users/Salah/Documents/GitHub/pyqgis/data/black-tailed.csv?delimiter=%s&xField=%s&yField=%s&crs=epsg:4326" % (",", "location-long", "location-lat")
csvLayer = QgsVectorLayer(url, "birds", "delimitedtext")

# Filter
csvLayer.setSubsetString("\"individual-local-identifier\" = 'Rotterdam'")

# Define the source and destination CRS
sourceCrs = QgsCoordinateReferenceSystem("EPSG:4326")
destinationCrs = QgsCoordinateReferenceSystem("EPSG:3857")

# Create a coordinate transform
transform = QgsCoordinateTransform(sourceCrs, destinationCrs, QgsProject.instance())

COORDS = []
for feature in csvLayer.getFeatures():
    geom = feature.geometry()
    geom.transform(transform)
    if geom:
        c = [geom.asPoint().x(), geom.asPoint().y()]
        COORDS.append(c)

clustering = DBSCAN(eps=15000, min_samples=25).fit(COORDS)
labels = clustering.labels_
print(len(labels))

layerCluster = QgsVectorLayer("MultiPoint?crs=epsg:3857", "Zone arrêt", "memory")
cur = layerCluster.dataProvider()
layerCluster.startEditing()

cur.addAttributes( [
    QgsField("num", QVariant.String),
    QgsField("nbpt", QVariant.Int)
])

for numCluster in set(labels):
    if numCluster == -1:
        continue
    POINTS = []
    for i in range(len(labels)):
        if labels[i] == numCluster:
            coord = COORDS[i]
            point = QgsPointXY(coord[0], coord[1])
            POINTS.append(point)
            cluster = QgsFeature()
            geomCluster = QgsGeometry.fromMultiPointXY(POINTS)
            cluster.setGeometry(geomCluster)
            cluster.setAttributes(["arret " + str(numCluster), len(POINTS)])
            # Enn on l’ajoute on fournisseur de la couche
            cur.addFeature(cluster)

    layerCluster.commitChanges()

QgsProject.instance().addMapLayer(layerCluster)
