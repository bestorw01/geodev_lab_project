# Data Notes

## GRID3_Nigeria_-_Local_Government_Area_Boundaries.shp
- Source: https://data.grid3.org
- Downloaded: 9th September, 2026
- 774 Features Polygon
- Columns: FID (Integer), globalid (String), uniq_id (Integer), timestamp(Date), editor(String), lganame(String), lgacode(String), statename (String), statecode (String), source (String), amapcode (String), Shape__Are (Real), Shape__Len (Real)
- No null in LGA Names
- It covers my LGA fully

## GRID3_Nigeria_-_Ward_Boundaries.shp
- Source: https://data.grid3.org
- Downloaded: 9th September, 2026
- 9,410 Features Polygon
- Columns: FID (Integer), globalid (String), uniq_id (Integer), timestamp(Date), editor(String), wardname (String), wardcode (String), lganame(String), lgacode(String), statename (String), statecode (String), source (String), amapcode (String), status (String), urban (String), Shape__Are (Real), Shape__Len (Real)
- No null in Ward Names
- It covers my Wards fully

## Jos_south_LGA_Roads via QuickOSM
- Query: highway=* within Jos South LGA extend
- Extracted: 10th September, 2026
- 3,570 features, Line
- Most of the line have no surface tags, therefore paved and unpaved way cannot be separated everywhere
- Road coverage looks good in the built-up areas especially in the Northern part, and sparse at the edges.

## Nigeria_-_Settlement_Points.shp
- Source: https://data.grid3.org
- Downloaded: 9th September, 2026
- 292,438 Features Points
- Columns: FID (Integer), globalid (String), uniq_id (Integer), timestamp(Date), scdy_editor (String), wardname (String), wardcode (String), lganame(String), lgacode(String), statename (String), statecode (String), set_altnam (String), set_id (String), set_name (String), is_primary (String), source (String) 
- No null in Settlement point Names
- It covers my area of study fully

## Nigeria_-_Health_Care_Facilities_.shp
- Source: https://data.grid3.org
- Downloaded: 9th September, 2026
- 46,146 Features Points
- Columns: FID (Integer), globalid (String), uniq_id (Integer), timestamp(Date), editor (String), latitude (Real), longitude (Real), wardname (String), wardcode (String), lganame(String), lgacode(String), statename (String), statecode (String), updated_on (Date), accessblty (String), func_stats (String), category (String), ownership (String), type (String), source (String), alt_name (String), prmry_name (String)
- No null in Settlement point Names
- It covers my area of study fully
