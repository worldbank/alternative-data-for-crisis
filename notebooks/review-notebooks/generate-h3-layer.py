import geopandas as gpd
import h3
from shapely.geometry import shape

argentina = gpd.read_file("C:/Users/Usuario/Downloads/gadm41_ARG_1.json") # load 
san_juan = argentina[argentina['NAME_1'] == 'SanJuan'].to_crs(epsg=4326) # filter
san_juan_geom = san_juan.geometry.values[0] # geometry

# Get all level 6 H3 cell IDs covering San Juan polygon
hex_ids = h3.geo_to_cells(san_juan_geom, res=6)

# For each cell, get shapely polygon via cells_to_h3shape
def cell_to_shapely(cell):
    h3shape = h3.cells_to_h3shape([cell])  # returns LatLngPoly or LatLngMultiPoly
    return shape(h3shape.__geo_interface__) # convert to shapely Polygon or MultiPolygon

# Create a GeoDataFrame with one polygon per hex cell
hex_geometries = [cell_to_shapely(h) for h in hex_ids]
gdf_hexes = gpd.GeoDataFrame({'h3_index': hex_ids, 'geometry': hex_geometries}, crs='EPSG:4326')

#print(f"Number of hexagons: {len(gdf_hexes)}")
#gdf_hexes.plot(edgecolor='black', facecolor='none', figsize=(10, 10))

gdf_hexes.to_file("san_juan_hexagons.geojson", driver="GeoJSON")