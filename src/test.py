import csv


with open('breeds_data.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        data.append({
            'title': row['title'],
        })

print(data)