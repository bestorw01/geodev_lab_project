with open("wards.csv", "r") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area = parts[1]
    area_km2 = float(parts[1])
    area_hectares = area_km2 * 100

    if area_km2 > 9:
        size = "large"
    else:
        size = "small"

    print(ward, "is", size, " in hectares")
