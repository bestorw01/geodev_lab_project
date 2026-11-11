import geopandas as gpd
import pandas as pd

print(pd.set_option("display.max_columns", None))
print(gpd.read_file("data/processed/Healthcare_facilities.gpkg"))
wards = gpd.read_file("data/processed/Healthcare_facilities.gpkg", layer="wards")

print(wards.head())
print("Rows and Columns: ", wards.shape)
print(wards.geom_type.value_counts())
print("Coordinate Reference System: ", wards.crs)
print("Bounds: ", wards.total_bounds)


