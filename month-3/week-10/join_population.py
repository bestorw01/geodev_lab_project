import pandas as pd
import geopandas as gpd

wards = gpd.read_file("./data/processed/wards.gpkg", layer="wards")
pop = pd.read_csv("./data/raw/ward_population.csv")

first = wards.merge(pop, left_on="ward_name", right_on="ward", how="left")
matched = first["population_2024"].notna().sum()
print("Matched: ", matched, "of", len(wards))

def clean_name(name):
    return name.strip().upper().replace(" ", "_")

wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("Matched after cleaning: ", matched, "of", len(wards))
print(joined[["ward_name", "population_2024"]])