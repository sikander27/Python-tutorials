"""
    Python Script to convert Dict to CSV
"""

import csv
import json
f = open('/Users/sikanderkhan/Desktop/eng_Rate_impact.json',)
impact = json.load(f)
rows = []
for key, value in impact.items():
    # value["influener_id"] = key
    rows.append(value)
keys = rows[0].keys()

with open('eng_impact.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(rows)