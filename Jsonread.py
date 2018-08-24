import json
file=open("zion.json", "r")
data=file.read()
PyData=json.loads(data)
print(data)
file.close()
