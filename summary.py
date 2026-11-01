import csv

def summerise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summaries(values)
    return report


#Read the file into rows
def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))
    
def clean_values(rows, columns):
    values = []
    for row in rows:
        raw = row[columns].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summaries(values):
    if len(values) == 0:
        return {"count":0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values)/len(values),
    }


# def summerise_all(filename, columns):
#     rows = read_rows(filename, columns)
#     report = {}
#     for column in columns:
#         values = clean_values(rows, column)
#         report[column] = summaries(values)
#     return report

report = summerise_all("Jos-South_Wards.csv", ["area_km2", "area_m2"])

for column, stats in report.items():
    print(column, "->", stats)



rows = read_rows("Jos-South_Wards.csv")
values = clean_values(rows, "area_km2")
result = summaries(values)

print(result)

