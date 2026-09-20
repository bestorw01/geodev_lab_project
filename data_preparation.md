# data preparation

## CRS and Preparation
- All scource layers arrived in EPSG: 4326
- Study Area: Jos South, was extraced from Grid3 Nigeria wards data
- All layers are clipped to study area and reprojected from EPSG:4326 WGS84 to EPSG: 32632 (UTM 32N) 
- All data are save as GeoPackage (.gpkg) extension, this is to save data in a tabular format a single SQL Lite database container that supports massive datasets up to 140TB.
- Area Check: The area of Jos South LGA is 558.6 Km2, matches international published data figure, while locally published data are varies with 512 - 518 km2 (this can be based on the type shapefile used by the local publishers).
- Working files are saved in data/processed/, while raw files are untouched and saved in data/raw.
- The data covers my area of study fully and it is mixed with but Primary Health Care, Private Owned Health Facilities, Clinics, Pharmacy and Dispensries.
