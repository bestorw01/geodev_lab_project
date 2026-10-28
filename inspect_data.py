import csv

# with open("Jos-South_Wards.csv", encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# print("Number of rows", len(rows))
#     raw = row["wardname"].strip()
# print("Columns ", list(rows[0].keys()))


# THSPECT ONE NUMBER COLUMN

# with open("Jos-South_Wards.csv", encoding="utf-8-sig") as f:
#     rows = csv.DictReader(f)

# values = []
# for row in rows:
#     value = float(row["wardname"])
#     values.apend(value)
# print("Samllest: ", min(values))
# print("", max(value))
# print("Count: ", len(value))
#     raw = row["wardname"].strip()


# HANDLNG EMPTY CELL

# with open("Jos-South_Wards.csv", encoding="utf-8-sig") as f:
#     rows = csv.DictReader(f)

# values = []
# for row in rows:
#     raw = row["wardname"].strip()
#     if raw == "":
#         continue
#     values.append(float(raw))   
    
# print("Samllest: ", min(values))
# print("largest ", max(values))
# print("Count: ", len(values))

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))  
    return {"Samllest" : min(values),
            "largest" : max(values),
            "Count" : len(values),
            "Avarage" : sum(values)/len(values)}

area_result = inspect_column("Jos-South_Wards.csv", "area_km2")

print(area_result)