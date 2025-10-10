import json
data = json.load(open("file.json"))
json.dump(data, open("out.json","w"))
