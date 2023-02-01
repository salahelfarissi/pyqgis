import geopandas
from shapely.geometry import LineString
import pandas as pd
import os

def match(geom1, geom2, threshold1, threshold2):
    if geom1.intersects(geom2):
        g1 = geom1.intersection(geom2)
        area = g1.area
        return area > threshold1/2.0 and area > threshold2 * min(geom1.area, geom2.area)
    return False

def match_tables(table1, table2, threshold):
    min_area = min(table1['geometry'].apply(lambda x: x.area).min(),table2['geometry'].apply(lambda x: x.area).min())
    newdata = pd.DataFrame(columns = ['id', 'id1', 'id2', 'geometry'])
    count = 0
    for index1, row1 in table1.iterrows():
        g1 = row1['geometry']
        if count == 1:
            break
        for index2, row2 in table2.iterrows():
            g2 = row2['geometry']
            if match(g1, g2, min_area, threshold):
                line = LineString([g1.centroid,g2.centroid])
                newmatch = {'id':len(newdata), 'id1':index1, 'id2':index2, 'geometry':line}
                print(newmatch, type(newmatch))
                newdata.loc[len(newdata)] = newmatch
                if newmatch['id'] == 20:
                    count = 1
                    break
    print("Final count = ", len(newdata))
    print("Dataframe Contents ", newdata, sep='\n')
    return geopandas.GeoDataFrame(newdata, geometry='geometry')

p1 = geopandas.read_file('data/donnees_tp_2022_2023/ilots_verniquet.shp')
p2 = geopandas.read_file('data/donnees_tp_2022_2023//ilots_vasserot.shp')

print(p1.crs)
print(p2.crs)
newdata = match_tables(p1,p2,0.2)
newdata.crs = p1.crs
os.mkdir('./data/match')
newdata.to_file('./data/match/match.shp')
