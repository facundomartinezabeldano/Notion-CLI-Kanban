import json
userdata = open("src/userdata.json","r")
data = json.load(userdata)
print(data)