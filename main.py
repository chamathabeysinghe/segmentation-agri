import json

with open('data2/train/via_region_data.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

for key, value in data.items():
    print(value)



