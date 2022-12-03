from qgis.core import QgsDistanceArea, QgsPointXY

# Calculate the ellipsoidal distance between two points
taza = (34.2106, 3.9980)
rabat = (33.9716, 6.8498)

d = QgsDistanceArea()
d.setEllipsoid('WGS84')

lat1, lon1 = taza
lat2, lon2 = rabat

point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

d = d.measureLine([point1, point2])
print(f"{d/1000:.2f} km")