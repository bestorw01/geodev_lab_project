import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("./data/processed/wards.gpkg", layer="wards")
facilities = gpd.read_file("./data/processed/facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(10, 10))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Health Facilities in Ibadan North", fontsize=16)
ax.set_axis_off()

fig.savefig("./data/processed/facilities_map.png", dpi=300, bbox_inches="tight")