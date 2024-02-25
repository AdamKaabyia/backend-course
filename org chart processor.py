import json

f = open('org_chart_large.json', "r")

data = json.loads(f.read())

for i in data['name']:
    print(i)

f.close()