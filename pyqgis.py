from qgis.core import QgsDistanceArea, QgsPointXY, QgsUnitTypes

# Calculate the ellipsoidal distance between two points with a stop
taza = (34.2106, 3.9980)
rabat = (33.9716, 6.8498)
fes = (34.0181, 5.0078)

d = QgsDistanceArea()
d.setEllipsoid('WGS84')

lat1, lon1 = taza
lat2, lon2 = rabat
lat3, lon3 = fes

point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)
point3 = QgsPointXY(lon3, lat3)

distance = d.measureLine([point1, point3]) + d.measureLine([point3, point2])
print(f"{d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceKilometers):.3f} km")