p = open("Survey.py", "w")
p.write(data)
p.close()

         
json = "Json.py"
jsonData = {'Name':[], 'Age':[], 'Place':[], 'X':[]}
pyjson = json.loads(jsonData)
