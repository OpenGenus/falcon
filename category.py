import os
import json

repoDir = os.path.dirname(os.path.abspath(__file__)) +"/cosmos"
category = []

def dirParser(path):
    dirs = path.split("/")
    try:
        if dirs[-2]== "test" or dirs[-2] == "src":
            description = dirs[-3] + " " + dirs[-1]
        else:
            description = dirs[-2] + " " + dirs[-1]
    except:
        description = ' '.join(dirs)
     
    dirName = dirs[-1]
    description = description.replace("_"," ")
    dirName = dirName.replace("_"," ")
    obj = {
        "dirName" : dirName,
        "description" : description
    }
    return obj
def path_to_dict(path):
    d = {'name': path}
    if os.path.isdir(path):
        parsedDetails = dirParser(os.path.join(path))
        temp = {
            "description" : parsedDetails["description"],
            "category" : parsedDetails["dirName"],
            "location" : os.path.join(path)
        }
        category.append(temp)
        [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    return category


with open('category.json', 'w') as outfile:
    json.dump(path_to_dict(repoDir), outfile)
    print("done")