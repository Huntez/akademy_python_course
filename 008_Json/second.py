import os.path
import json

file = open(os.path.join("lesson14", "second.json"), "w")
sdict = {
    "Ivan": {"sname":"Sidorov", "age":"14"}
}
json.dump(sdict,file); file.close()

file = open(os.path.join("lesson14", "second.json"), "r")
svar = json.load(file); print(svar)
